"""register models to site."""

from django.contrib import admin
from .models import (
    Animal,
    Purchased,
    LocallyServiced,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServiceAnimal,
    MedicineTreatment,
    Dosagetreatment,
)

admin.site.register(Animal)
admin.site.register(Purchased)
admin.site.register(LocallyServiced)
admin.site.register(AIPredeterminedServiceAnimal)
admin.site.register(AInonPredeterminedServiceAnimal)
admin.site.register(MedicineTreatment)
admin.site.register(Dosagetreatment)
