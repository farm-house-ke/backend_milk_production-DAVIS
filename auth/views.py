"""urls for auth app."""

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(generics.CreateAPIView):
    """view for user registration."""

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": RegisterSerializer(
                    user, context=self.get_serializer_context()
                ).data
            },
            status=status.HTTP_201_CREATED,
        )


class MyObtainTokenPairView(TokenObtainPairView):
    """view for obtaining token pair."""

    serializer_class = MyTokenObtainPairSerializer
