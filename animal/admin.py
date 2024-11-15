"""register models to site."""

from django.contrib import admin
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    MedicineTreatment,
    DosageTreatment,
    ProductionBase
)


admin.site.register(PurchasedAnimal)
admin.site.register(LocallyServicedAnimal)
admin.site.register(MedicineTreatment)
admin.site.register(DosageTreatment)
admin.site.register(ProductionBase)