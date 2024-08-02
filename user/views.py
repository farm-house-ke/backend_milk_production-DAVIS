"""views for user model."""

from django.contrib.auth import login, get_user_model
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

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
                "user_id": user.id,
                "username": user.username,
            },
            status=status.HTTP_200_OK,
        )

class LogoutView(APIView):
    """logout view."""
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """logout user."""
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)