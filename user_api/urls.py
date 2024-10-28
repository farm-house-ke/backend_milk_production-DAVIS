from django.urls import path
from .views import UserViewSet, ProfileImageUploadView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", UserViewSet.as_view({"post": "register"}), name="register"),
    path("login/", UserViewSet.as_view({"post": "login"}), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "upload-profile-image/",
        ProfileImageUploadView.as_view(),
        name="uploads-profile-image",
    ),  # url handling for profile view
]
