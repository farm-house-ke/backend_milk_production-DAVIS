"""register models to site."""

from django.contrib import admin
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServicedAnimal,
    MedicineTreatment,
    DosageTreatment,
)


admin.site.register(PurchasedAnimal)
admin.site.register(LocallyServicedAnimal)
admin.site.register(AIPredeterminedServiceAnimal)
admin.site.register(AInonPredeterminedServicedAnimal)
admin.site.register(MedicineTreatment)
admin.site.register(DosageTreatment)
