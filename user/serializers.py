"""serializer for user model."""
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()

class UserSignUpSerializer(serializers.ModelSerializer):
    """sign up serializer."""
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ["id", "email","username", "password"]

    def create(self, validated_data):
        """create user."""
        user = User.objects.create_user(
            email = validated_data["email"],
            username = validated_data["username"],
            password = validated_data["password"],
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid login credentials")
        else:
            raise serializers.ValidationError('Must include "username" and "password"')

        data["user"] = user
        return data
