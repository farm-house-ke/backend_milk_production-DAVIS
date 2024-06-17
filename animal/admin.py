"""register models to site."""

from django.contrib import admin
from .models import (
    Animal,
    Purchased,
    LocallyServiced,
    AIPredeterminedServiced,
    AInotPredeterminedServiced,
    TreatmentRecords,
    MedicineTreatment,
    Dosagetreatment,
)

admin.site.register(Animal)
admin.site.register(Purchased)
admin.site.register(LocallyServiced)
admin.site.register(AIPredeterminedServiced)
admin.site.register(AInotPredeterminedServiced)
admin.site.register(TreatmentRecords)
admin.site.register(MedicineTreatment)
admin.site.register(Dosagetreatment)
