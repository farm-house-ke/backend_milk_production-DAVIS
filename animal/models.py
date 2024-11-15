from django.db import models
from django.utils import timezone
from django.db import models
from datetime import timedelta
from django.core.validators import (
    MinLengthValidator,
)


class AnimalBase(models.Model):
    """Base model for all animal models"""

    animal_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    image = models.ImageField(
        upload_to="static/", blank=False, default="static/default.jpg"
    )
    weight = models.FloatField(default=0.0)
    breed = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    gender = models.CharField(max_length=1, choices=[("M", "male"), ("F", "female")])
    date_of_next_service = models.DateField(
        null=True,
        blank=True,
        help_text="Only applicable for female",
        default=timezone.now,
    )
    daughter_of = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        null=True,
        blank=True,
        help_text="Only applicable if gender is female",
    )
    son_of = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        null=True,
        blank=True,
        help_text="Only applicable if gender is male",
    )

    class Meta:
        pass

    def __str__(self):
        return self.animal_name


class PurchasedAnimal(AnimalBase):
    """Model for purchased animals"""

    date_of_birth = models.DateField(default=timezone.now())
    expected_maturity_date = models.DateField(default=timezone.now())
    seller_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    price_bought = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date_purchased = models.DateField(default=timezone.now())

    class Meta:
        verbose_name_plural = "Purchases"


class LocallyServicedAnimal(AnimalBase):
    """Model for locally serviced animals"""

    birth_date = models.DateField(default=timezone.now())
    expected_maturity_date = models.DateField(default=timezone.now())
    bull = models.CharField(
        max_length=50, validators=[MinLengthValidator(2)], default="Not specified"
    )
    name_of_owner = models.CharField(max_length=50, validators=[MinLengthValidator(2)])

    class Meta:

        verbose_name_plural= "local services"

        verbose_name = "locally_serviced"

class MedicineTreatment(models.Model):
    animal_name = models.ForeignKey(AnimalBase, on_delete=models.CASCADE)
    diagnosis_description = models.TextField(default="Not specified")
    date_of_diagnosis = models.DateField(default=timezone.now().date())
    name_of_vet = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    date_of_medication = models.DateField(default=timezone.now().date())
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
    date_sold = models.DateField(
        blank=True, null=True, help_text="Only applicable if animal is sold."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Only applicable if animal is sold.",
    )

    def __str__(self):
        return f"{self.animal_name} - {self.current_state} - {self.sold_status} - {self.date_of_medication} - {self.date_of_diagnosis} - {self.name_of_vet} - {self.diagnosis_description}"


class DosageTreatment(models.Model):
    animal_name = models.ForeignKey(AnimalBase, on_delete=models.CASCADE)
    diagnosis_description = models.TextField(default="Not specified")
    date_of_diagnosis = models.DateField(default=timezone.now().date())
    name_of_vet = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    dosage_treatment_used = models.CharField(
        max_length=50, validators=[MinLengthValidator(2)], default="Not specified"
    )
    date_of_medication = models.DateField()
    STATE_CHOICES = (("cured", "Cured"), ("dead", "Dead"))
    current_state = models.CharField(max_length=50, choices=STATE_CHOICES)
    SOLD_CHOICES = (("sold", "Sold"), ("not_sold", "Not Sold"))
    sold_status = models.CharField(
        max_length=50,
        choices=SOLD_CHOICES,
        blank=True,
        null=True,
    )
    date_sold = models.DateField(
        blank=True, null=True, help_text="Only applicable if animal is sold."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Only applicable if animal is sold.",
    )

    def __str__(self):
        return f"{self.animal_name} - {self.current_state} - {self.sold_status} - {self.date_of_medication} - {self.date_of_diagnosis} - {self.name_of_vet} - {self.dosage_treatment_used}"


class Disposal(models.Model):
    animal_name = models.ForeignKey(AnimalBase, on_delete=models.CASCADE)
    date_of_disposal = models.DateField(default=timezone.now())
    remark = models.TextField(default="Not specified")

    def __str__(self):
        return f"{self.animal_name} - {self.date_of_disposal} - {self.remark}"


class ServingBase(models.Model):
    """Base model for all serving models"""

    animal_name = models.ForeignKey(AnimalBase, on_delete=models.CASCADE)
    date_presented = models.DateField(default=timezone.now())
    STATUS_CHOICES = (("confirmed", "Confirmed"), ("aborted", "Aborted"))
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    expected_date_of_delivery = models.DateField(
        blank=True,
        null=True,
        help_text="Only applicable if status is confirmed.",
        default=timezone.now(),
    )

    def __str__(self):
        return f"{self.animal_name} - {self.date_presented}"


class Bull(ServingBase):
    """Model for bull serving"""

    name_of_bull = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    owner_of_bull = models.CharField(max_length=50, validators=[MinLengthValidator(2)])

    class Meta:
        verbose_name = "bull"


class ArtificialInsemination(ServingBase):
    """Model for artificial insemination"""

    vet_officer_name = models.CharField(
        max_length=50, validators=[MinLengthValidator(2)]
    )
    vet_number = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    OVA_CHOICES = (("predetermined", "Predetermined"), ("normal", "Normal"))
    ova = models.CharField(max_length=50, choices=OVA_CHOICES)

    class Meta:
        verbose_name = "artificial_insemination"


class ProductionBase(models.Model):
    """Model for animal milk production with individual calf quantities and sales logic"""

    animal_name = models.ForeignKey(AnimalBase, on_delete=models.CASCADE)
    quantity_am = models.IntegerField(default=0)  # Morning production (in liters)
    quantity_pm = models.IntegerField(default=0)  # Evening production (in liters)
    posho_quantity = models.IntegerField(default=0)  # Quantity for posho (in liters)
    sales_quantity = models.IntegerField(default=0)  # Quantity sold (in liters)
    load_quantity = models.IntegerField(default=0)  # Quantity loaded (in liters)
    deals_quantity = models.IntegerField(default=0)  # Quantity for deals (in liters)
    daily_total = models.IntegerField(
        default=0
    )  # Total production for the day (in liters)
    balance_quantity = models.IntegerField(
        default=0
    )  # Balance after adjustments (in liters)
    carried_over_quantity = models.IntegerField(
        default=0
    )  # Remaining carried to the next day (in liters)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_daily_total(self):
        """Calculate the total production for the day (AM + PM, in liters)."""
        return self.quantity_am + self.quantity_pm

    def get_total_quantity_taken_by_calves(self):
        """Sum up the quantity taken by all calves (in liters)."""
        total_quantity_taken_by_calves = sum(
            calf.quantity_taken for calf in self.calves.all()
        )
        return total_quantity_taken_by_calves

    def get_adjusted_balance(self):
        """Calculate balance after posho and calves (in liters)."""
        total_calves_quantity = self.get_total_quantity_taken_by_calves()
        adjusted_balance = self.get_daily_total() - (
            self.posho_quantity + total_calves_quantity
        )
        return adjusted_balance

    def get_sales_balance(self):
        """Calculate the balance after sales, loads, and deals (in liters)."""
        adjusted_balance = self.get_adjusted_balance()
        sales_balance = adjusted_balance - (
            self.sales_quantity + self.load_quantity + self.deals_quantity
        )
        return sales_balance

    def calculate_balance(self):
        """Final calculation of balance and handling carried-over quantity (in liters)."""
        final_balance = self.get_sales_balance()
        if final_balance == 0:
            self.balance_quantity = 0
        else:
            self.balance_quantity = final_balance
            self.carried_over_quantity = (
                final_balance  # Carry over to the next day if not 0 (in liters)
            )
        return self.balance_quantity

    def save(self, *args, **kwargs):
        """Override save method to store calculated totals and balance (in liters)."""
        self.daily_total = self.get_daily_total()
        self.balance_quantity = self.calculate_balance()
        super().save(*args, **kwargs)  # Save the model after updating totals


class Calf(models.Model):
    """Model for individual calves and their milk consumption (in liters)"""

    calf_name = models.CharField(max_length=100)
    quantity_taken = models.IntegerField(
        default=0
    )  # Quantity taken by this calf (in liters)

    def __str__(self):
        return f"{self.calf_name} took {self.quantity_taken} liters"
