"""register models to site."""

from django.contrib import admin
from .models import (
    AnimalBase,
    PurchasedAnimal,
    LocallyServicedAnimal,
    MedicineTreatment,
    DosageTreatment,
    ProductionBase,
    Calf,
)

admin.site.register(AnimalBase)
admin.site.register(PurchasedAnimal)
admin.site.register(LocallyServicedAnimal)
admin.site.register(MedicineTreatment)
admin.site.register(DosageTreatment)
admin.site.register(ProductionBase)
admin.site.register(Calf)