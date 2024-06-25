from django.db import models
from django.utils import timezone
from django.core.validators import (
    MinLengthValidator,
)


class Animal(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    SOURCE_CHOICES = (
        ("purchased", "Purchased"),
        ("locally_serviced", "Locally Serviced"),
        ("ai_predetermined", "AI Predetermined"),
        ("ai_non_predetermined", "AI not Predetermined"),
    )

    name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    image = models.ImageField(
        upload_to="static/", null=True, blank=True, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(max_length=1, choices=[("M", "male"), ("F", "female")])
    date_of_next_service = models.DateField(
        null=True, blank=True, help_text="Only applicable for female"
    )
    source = models.CharField(null=True, max_length=50, choices=SOURCE_CHOICES)

    def __str__(self):
        return f"{self.name}"


class Purchased(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_purchased = models.DateField(default=timezone.now)

    def __str__(self):
        return self.animal.name


class LocallyServiced(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name_of_owner = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_of_service = models.DateField(default=timezone.now)
    birth_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.animal.name


class AIPredeterminedServiceAnimal(models.Model):
    """Model for AI predetermined serviced animals."""

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date_of_service = models.DateField(default=timezone.now)
    birth_date = models.DateField(default=timezone.now)
    gender = models.CharField(
        max_length=10, choices=[("female", "Female")], default="female"
    )
    date_of_next_service = models.DateField(
        null=True, blank=True, help_text="only applicable for female"
    )

    def __str__(self):
        return self.animal.name


class AInonPredeterminedServiceAnimal(models.Model):
    """Model for AI not predetermined serviced animals."""

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date_of_service = models.DateField(default=timezone.now)
    birth_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.animal.name


class MedicineTreatment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date_of_diagnosis = models.DateField(default=timezone.now)
    name_of_vet = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(
                2, message="Name of vet must be at least 2 characters long."
            )
        ],
    )
    date_of_medicine_treatment = models.DateField(default=timezone.now)
    current_state = models.CharField(
        max_length=1, choices=(("D", "dead"), ("C", "cured"))
    )
    cured = models.CharField(max_length=1, choices=(("S", "sold"), ("N", "not sold")))

    def __str__(self):
        return f"{self.animal.name} - {self.date_of_diagnosis.strftime('%Y-%m-%d')} - {self.name_of_vet} - {self.date_of_medicine_treatment.strftime('%Y-%m-%d')} - {self.current_state} - {self.cured}"


class Dosagetreatment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date_of_diagnosis = models.DateField(default=timezone.now)
    name_of_vet = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_of_medicine_treatment = models.DateField(default=timezone.now)
    dosage_treatment_used = models.CharField(
        max_length=50, validators=[MinLengthValidator(2)]
    )
    current_state = models.CharField(
        max_length=1, choices=(("D", "dead"), ("C", "cured"))
    )
    cured = models.CharField(max_length=1, choices=(("S", "sold"), ("N", "not sold")))

    def __str__(self):
        return f"{self.animal.name} - {self.date_of_diagnosis.strftime('%Y-%m-%d')} - {self.name_of_vet} - {self.date_of_medicine_treatment.strftime('%Y-%m-%d')} - {self.dosage_treatment_used} - {self.current_state} - {self.cured}"
