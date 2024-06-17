"""tests for auth app"""
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .serializers import RegisterSerializer


class RegisterSerializerTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            "username": "testuser",
            "password": "testpassword123",
            "password2": "testpassword123",
            "email": "testuser@gmail.com",
            "first_name": "Test",
            "last_name": "User",
        }

    def test_can_register_user(self):
        response = self.client.post("/api/register/", self.valid_payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")

    def test_passwords_must_match(self):
        self.valid_payload["password2"] = "wrongpassword"
        serializer = RegisterSerializer(data=self.valid_payload)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(["password"]))
