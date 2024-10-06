import logging
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from .serializers import UserSignUpSerializer, UserLoginSerializer

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["post"])
    def register(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            refresh = RefreshToken.for_user(user)
            logger.debug(f"User registered: {user.username}")
            return Response(
                {
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                    "user": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        logger.error(f"Registration error: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            login(request, serializer.validated_data["user"])
            logger.debug(
                f"User logged in: {serializer.validated_data['user'].username}"
            )
            return Response(
                {
                    "access_token": serializer.validated_data["access_token"],
                    "refresh_token": serializer.validated_data["refresh_token"],
                    "username": serializer.validated_data["user"].username,
                },
                status=status.HTTP_200_OK,
            )
        logger.error(f"Login error: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
