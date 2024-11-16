from django.db import models
from django.utils import timezone
from django.db import models
from datetime import timedelta,date
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
    local_sales_quantity = models.IntegerField(default=0)  # Quantity sold locally (in liters)
    dealers_sales_quantity = models.IntegerField(default=0)  # Quantity sold to dealers (in liters)
    balance_quantity = models.IntegerField(default=0)  # Balance after sales (in liters)_quantity
    carried_over_quantity=models.IntegerField(default=0)
    date=models.DateField(default=date.today)#record the date
    timestamp=models.DateTimeField(auto_now_add=True)#record the timestamp/record of creation
    
    def get_daily_production(self):
        # Calculate the daily production(morning + evening)
        return self.quantity_am + self.quantity_pm
    
    def get_total_sales(self):
        # Calculate the total sales (local + dealers)
        return self.local_sales_quantity + self.dealers_sales_quantity
    
    def get_total_deductions(self):
        # Calculate the total deductions ( posho + calves feed)
        total_calves_feed=sum(calf.quantity_taken for calf in self.calves.all())
        return self.posho_quantity + total_calves_feed
    
    def calculate_balance(self):
        #Calculate the balance:
        #Total production - Total sales - Total deductions
        #if balance !=0: carried over

        total_production=self.get_daily_production()
        total_sales=self.get_total_sales()
        total_deductions=self.get_total_deductions()    

        #calculating  balance
        balance=total_production-total_sales-total_deductions

        if balance < 0:
            raise ValueError("Balance cannot be negative.Please Check your Data")
        
        #ucarried over quantity
        if balance == 0:
            self.carried_over_quantity=0    
        else:
            self.carried_over_quantity=balance
        
        return balance
    
    def save(self, *args, **kwargs):
        #ovveride save method to perform calculations before saving
        self.balance_quantity=self.calculate_balance()
        super().save(*args, **kwargs)


class Calf(models.Model):
    """Model for individual calves and their milk consumption (in liters)"""
    animal=models.ForeignKey(AnimalBase,on_delete=models.CASCADE,related_name='calves')
    calf_name = models.CharField(max_length=100)
    quantity_taken = models.IntegerField(
        default=0
    )  # Quantity taken by this calf (in liters)
    timestamp=models.DateTimeField(auto_now_add=True)#record the timestamp/record of creation

    def __str__(self):
        return f"{self.calf_name} (Animal:{self.animal.animal_name}) took {self.quantity_taken} liters of milk"
