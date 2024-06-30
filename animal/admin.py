"""register models to site."""

from django.contrib import admin
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServiceAnimal,
)


admin.site.register(PurchasedAnimal)
admin.site.register(LocallyServicedAnimal)
admin.site.register(AIPredeterminedServiceAnimal)
admin.site.register(AInonPredeterminedServiceAnimal)
