from django.urls import path
from .views import UserLoginView, UserList

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserList.as_view(), name="users"),
]
