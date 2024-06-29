"""register models to site."""

from django.contrib import admin
from .models import (
    Animal,
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServiceAnimal,
    MedicineTreatment,
    Dosagetreatment,
)

admin.site.register(Animal)
admin.site.register(PurchasedAnimal)
admin.site.register(LocallyServicedAnimal)
admin.site.register(AIPredeterminedServiceAnimal)
admin.site.register(AInonPredeterminedServiceAnimal)
admin.site.register(MedicineTreatment)
admin.site.register(Dosagetreatment)
