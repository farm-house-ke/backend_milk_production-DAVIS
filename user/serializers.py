"""serializer for user model."""
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSignUpSerializer(serializers.ModelSerializer):
    """sign up serializer."""
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["email","username", "password"]
    
    def create(self, validated_data):
        """create user."""
        user = User.objects.create_user(
            email = validated_data["email"],
            username = validated_data["username"],
            password = validated_data["password"],
        )
        return user