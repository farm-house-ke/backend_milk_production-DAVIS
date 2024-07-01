from django.db import models
from django.utils import timezone
from django.core.validators import (
    MinLengthValidator,
)


class PurchasedAnimal(models.Model):
    animal_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    image = models.ImageField(
        upload_to="static/", blank=False, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(max_length=1, choices=[("M", "male"), ("F", "female")])
    date_of_next_service = models.DateField(
        null=True,
        blank=False,
        help_text="Only applicable for female",
        default=timezone.now(),
    )
    seller_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_purchased = models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.animal_name}"


class LocallyServicedAnimal(models.Model):
    """Model for locally serviced animals"""

    animal_name = models.CharField(
        blank=False, max_length=50, validators=[MinLengthValidator(2)]
    )
    image = models.ImageField(
        upload_to="static/", blank=False, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(max_length=1, choices=[("M", "male"), ("F", "female")])
    date_of_next_service = models.DateField(
        null=True,
        blank=False,
        help_text="Only applicable for female",
        default=timezone.now(),
    )
    name_of_owner = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_of_service = models.DateField(default=timezone.now())
    birth_date = models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.animal_name}"


class AIPredeterminedAndNonPredeterminedServiceAnimal(models.Model):
    """Model for AI predetermined serviced animals."""

    animal_name = models.CharField(
        blank=False, max_length=50, validators=[MinLengthValidator(2)]
    )
    image = models.ImageField(
        upload_to="static/", blank=False, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(
        max_length=1,
        blank=False,
        choices=[("M", "male"), ("F", "female")],
        default="female",
    )
    date_of_next_service = models.DateField(
        null=True,
        blank=False,
        help_text="only applicable for female",
        default=timezone.now(),
    )
    date_of_service = models.DateField(
        default=timezone.now(),
    )
    birth_date = models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.animal_name}"
