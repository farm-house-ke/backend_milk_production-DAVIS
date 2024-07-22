"""views for user model."""

from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import UserSignUpSerializer

User = get_user_model()
class UserLoginView(APIView):
    """view for login user"""
    def post(self, request):
        """login user."""
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        if user:
            token = AccessToken.for_user(user)
            return Response({"token": str(token)})
        else:
            return Response({"error": "wrong credentials"}, status=400)

class UserList(generics.ListCreateAPIView):
    """view for user list."""
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer