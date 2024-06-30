from django.db import models
import datetime
from django.core.validators import (
    MinLengthValidator,
)


class PurchasedAnimal(models.Model):
    animal_name = models.CharField(
        null=True, blank=True, max_length=50, validators=[MinLengthValidator(2)]
    )
    image = models.ImageField(
        upload_to="static/", null=True, blank=True, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(max_length=1, choices=[("M", "male"), ("F", "female")])
    date_of_next_service = models.DateField(
        null=True, blank=True, help_text="Only applicable for female"
    )
    seller_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_purchased = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.animal_name}"


class LocallyServicedAnimal(models.Model):
    """Model for locally serviced animals"""

    animal_name = models.CharField(
        null=True, blank=True, max_length=50, validators=[MinLengthValidator(2)]
    )
    image = models.ImageField(
        upload_to="static/", null=True, blank=True, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(max_length=1, choices=[("M", "male"), ("F", "female")])
    date_of_next_service = models.DateField(
        null=True, blank=True, help_text="Only applicable for female"
    )
    name_of_owner = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_of_service = models.DateField(default=datetime.date.today)
    birth_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.animal_name}"


class AIPredeterminedServiceAnimal(models.Model):
    """Model for AI predetermined serviced animals."""

    animal_name = models.CharField(
        null=True, blank=True, max_length=50, validators=[MinLengthValidator(2)]
    )
    image = models.ImageField(
        upload_to="static/", null=True, blank=True, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(
        max_length=1, null=True, blank=True, choices=[("M", "male"),("F", "female")], default="female"
    )
    date_of_next_service = models.DateField(
        null=True, blank=True, help_text="only applicable for female"
    )
    date_of_service = models.DateField(default=datetime.date.today)
    birth_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.animal_name}"


class AInonPredeterminedServiceAnimal(models.Model):
    """Model for AI not predetermined serviced animals."""

    animal_name = models.CharField(
        null=True, blank=True, max_length=50, validators=[MinLengthValidator(2)]
    )
    image = models.ImageField(
        upload_to="static/", null=True, blank=True, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(max_length=1, choices=[("M", "male"), ("F", "female")])
    date_of_next_service = models.DateField(
        null=True, blank=True, help_text="Only applicable for female"
    )
    date_of_service = models.DateField(default=datetime.date.today)
    birth_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.animal_name}"
