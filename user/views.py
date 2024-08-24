"""views for user model."""

from django_ratelimit.decorators import ratelimit
from .serializers import UserSignUpSerializer, UserLoginSerializer
from django.contrib.auth import login, get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from django.core.cache import cache

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    @ratelimit(key="ip", rate="5/m", block=True)
    @action(detail=False, methods=["post"], serializer_class=UserLoginSerializer)
    def login(self, request):
        """Login user."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")

        if not user:
            return Response(
                {"details": "User not found"}, status=status.HTTP_400_BAD_REQUEST
            )

        login_attempts = cache.get(f"login_attempts_{user.id}", 0)
        if login_attempts > 5:
            return Response(
                {"details": "Account failed due to many logins"},
                status=status.HTTP_403_FORBIDDEN,
            )

        login(request, user)
        refresh = RefreshToken.for_user(user)

        cache.set(f"login_attempts_{user.id}", 0)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )
