from django.db import models
from django.utils import timezone


class Animal(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    image = models.ImageField(
        upload_to="static/", null=True, blank=True, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[("M", "male"), ("F", "female")])
    date_of_next_service = models.DateField(
        null=True, blank=True, help_text="Only applicable for female"
    )

    def __str__(self):
        return self.name


class Purchased(models.Model):
    """Model for purchased animals."""

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=50)
    date_purchased = models.DateField(default=timezone.now)

    def __str__(self):
        return self.animal


class LocallyServiced(models.Model):
    """Model for locally serviced animals."""

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name_of_owner = models.CharField(max_length=50)
    date_of_service = models.DateField(default=timezone.now)
    birth_date = models.DateField()

    def __str__(self):
        return self.animal


class AIPredeterminedServiced(models.Model):
    """Model for AI predetermined serviced animals."""

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date_of_service = models.DateField(default=timezone.now)
    birth_date = models.DateField()
    gender = models.CharField(
        max_length=10, choices=[("female", "Female")], default="female"
    )
    date_of_next_service = models.DateField(
        null=True, blank=True, help_text="only applicable for female"
    )

    def __str__(self):
        return self.animal


class AInotPredeterminedServiced(models.Model):
    """Model for AI not predetermined serviced animals."""

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date_of_service = models.DateField(default=timezone.now)
    birth_date = models.DateField(max_length=50)

    def __str__(self):
        return self.animal
