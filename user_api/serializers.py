from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def validate_password(self, value):
        """Validate the password using Django's password validators."""
        validate_password(value)
        return value

    def create(self, validated_data):
        """Create the user with the validated data."""
        is_staff = validated_data.pop("is_staff", False)
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return {
                "user": user,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            }
        raise serializers.ValidationError("Invalid credentials")
