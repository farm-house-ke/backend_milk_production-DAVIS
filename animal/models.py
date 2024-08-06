from django.db import models
from django.utils import timezone
from django.core.validators import (
    MinLengthValidator,
)


class AnimalBase(models.Model):
    """Base model for all animal models"""

    animal_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    image = models.ImageField(
        upload_to="static/", blank=False, default="static/default.jpg"
    )
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(max_length=1, choices=[("M", "male"), ("F", "female")])
    date_of_next_service = models.DateField(
        null=True,
        blank=True,
        help_text="Only applicable for female",
        default=timezone.now,
    )

    class Meta:
        pass

    def __str__(self):
        return self.animal_name


class PurchasedAnimal(AnimalBase):
    """Model for purchased animals"""

    seller_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_purchased = models.DateField(default=timezone.now())
    
    class Meta:
        verbose_name = "purchased"


class LocallyServicedAnimal(AnimalBase):
    """Model for locally serviced animals"""

    name_of_owner = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_of_service = models.DateField(default=timezone.now())
    birth_date = models.DateField(default=timezone.now())

    class Meta:
        verbose_name = "locally_serviced"

class AIPredeterminedServiceAnimal(AnimalBase):
    """Model for AI predetermined serviced animals."""
    ai_gender = models.CharField(max_length=1, default="F", editable=False)
    date_of_service = models.DateField(
        default=timezone.now(),
    )
    birth_date = models.DateField(default=timezone.now())

    class Meta:
        verbose_name = "ai_predetermined"

class AInonPredeterminedServicedAnimal(AnimalBase):
    """Model for AI non predetermined serviced animals."""

    date_of_service = models.DateField(
        default=timezone.now(),
    )
    birth_date = models.DateField(default=timezone.now())

    class Meta:
        verbose_name = "ai_non_predetermined"


class MedicineTreatment(models.Model):
    animal_name = models.ForeignKey(AnimalBase, on_delete=models.CASCADE)
    date_of_diagnosis = models.DateField(auto_now_add=True)
    name_of_vet = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_of_medication = models.DateField(auto_now_add=True)
    STATE_CHOICES = (("cured", "Cured"), ("dead", "Dead"))
    current_state = models.CharField(max_length=50, choices=STATE_CHOICES)
    SOLD_CHOICES = (("sold", "Sold"), ("not_sold", "Not Sold"))
    sold_status = models.CharField(
        max_length=50,
        choices=SOLD_CHOICES,
        blank=True,
        null=True,
        help_text="Select only if animal is cured.",
    )


class DosageTreatment(models.Model):
    animal_name = models.ForeignKey(AnimalBase, on_delete=models.CASCADE)
    date_of_diagnosis = models.DateField(auto_now_add=True)
    name_of_vet = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_of_medication = models.DateField(auto_now_add=True)
    STATE_CHOICES = (("cured", "Cured"), ("dead", "Dead"))
    current_state = models.CharField(max_length=50, choices=STATE_CHOICES)
    SOLD_CHOICES = (("sold", "Sold"), ("not_sold", "Not Sold"))
    sold_status = models.CharField(
        max_length=50,
        choices=SOLD_CHOICES,
        blank=True,
        null=True,
        help_text="Select only if animal is cured.",
    )
    dosage_treatment_used = models.CharField(max_length=100, default="Not specified")

    def __str__(self):
        return f"{self.animal_name} - {self.current_state}"
