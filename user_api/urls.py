from django.urls import path
<<<<<<< HEAD
from .views import UserViewSet,ProfileImageUploadView
=======
from .views import UserViewSet
>>>>>>> 28003f5fd2e9db1febc66726152e4fdbecdb0168
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", UserViewSet.as_view({"post": "register"}), name="register"),
    path("login/", UserViewSet.as_view({"post": "login"}), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
<<<<<<< HEAD
    path('upload-profile-image/',ProfileImageUploadView.as_view(),name='uploads-profile-image'),#url handling for profile view
=======
>>>>>>> 28003f5fd2e9db1febc66726152e4fdbecdb0168
]
