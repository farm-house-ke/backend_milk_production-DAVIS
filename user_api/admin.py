"""registering the models to the admin panel."""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)