"""serializer for user model."""

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.core.exceptions import ValidationError

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    """sign up serializer."""

    password = serializers.CharField(write_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
    
    
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value    
    

    def create(self, validated_data):
        """create user."""
        
        self.validate_password(validated_data["password"])
        
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            data["user"] = user
            return data
        raise serializers.ValidationError("Invalid credentials")
