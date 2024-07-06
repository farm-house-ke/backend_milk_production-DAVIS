"""register models to site."""

from django.contrib import admin
from .models import PurchasedAnimal, LocallyServicedAnimal, AIPredeterminedServiceAnimal


admin.site.register(PurchasedAnimal)
admin.site.register(LocallyServicedAnimal)
admin.site.register(AIPredeterminedServiceAnimal)
