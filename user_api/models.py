from django.contrib.auth.models import User
from django.db import models


# created a profile models for image upload
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True
    )

    def __str__(self):
        return self.user.username
