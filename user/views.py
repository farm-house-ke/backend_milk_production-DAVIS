"""views for user model."""

from django.contrib.auth import login, get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
from django.core.cache import cache
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
        login_attempts = cache.get(f"login_attempts_{user.id}", 0)
        if login_attempts > 7:
            return Response ({"details": "Account failed due to many logins"})
        login(request, user)
        refresh = RefreshToken.for_user(user)
        
        cache.set(f"login_atempts_user{user.id}", 0)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
    
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)