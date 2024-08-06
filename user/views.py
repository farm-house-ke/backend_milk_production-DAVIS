"""views for user model."""

from django.contrib.auth import login, get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action

User = get_user_model()
from .serializers import UserSignUpSerializer, UserLoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for user model."""

    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    @action(detail=False, methods=["post"], serializer_class=UserLoginSerializer)
    def login(self, request):
        """Login user."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )
