"""registering the models to the admin panel."""
from django.contrib import admin
from .models import Profile
# register profile model in admin panel
admin.site.register(Profile)