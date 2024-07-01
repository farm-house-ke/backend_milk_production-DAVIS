"""register models to site."""

from django.contrib import admin
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedAndNonPredeterminedServiceAnimal,
)


admin.site.register(PurchasedAnimal)
admin.site.register(LocallyServicedAnimal)
admin.site.register(AIPredeterminedAndNonPredeterminedServiceAnimal)

