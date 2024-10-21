import logging
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
<<<<<<< HEAD
from .serializers import UserSignUpSerializer, UserLoginSerializer,UserProfileSerializer
from rest_framework.views import APIView
from .models import Profile
=======
from .serializers import UserSignUpSerializer, UserLoginSerializer
>>>>>>> 28003f5fd2e9db1febc66726152e4fdbecdb0168

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
<<<<<<< HEAD

#profile image upload view
class ProfileImageUploadView(APIView):
    def post(self,request,*args,**kwargs):
        profile=Profile.objects.get(user=request.user)
        profile.profile_image=request.FILES.get('profile_image')
        profile.save()
        return Response({'message':'profile image uploaded successfully'},status=status.HTTP_200_OK)
    
=======
>>>>>>> 28003f5fd2e9db1febc66726152e4fdbecdb0168
