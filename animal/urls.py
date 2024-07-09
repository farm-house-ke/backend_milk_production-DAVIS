"""urls for animal app."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PurchasedAnimalViewSet,
    LocallyServicedAnimalViewSet,
    AInonPredeterminedServiceAnimalViewSet,
    AIPredeterminedServiceAnimalViewSet,
    PurchasedDosageViewSet,
    PurchasedMedicineViewSet,
    LocallyServicedMedicineViewSet,
    LocallyServicedDosageViewSet,
    AIPredeterminedMedicineViewSet,
    AIPredeterminedDosageViewSet,
    AInonPredeterminedMedicineViewSet,
    AInonPredeterminedDosageViewSet,
)

router = DefaultRouter()
router.register(r"purchased_animal", PurchasedAnimalViewSet)
router.register(r"locally_serviced_animal", LocallyServicedAnimalViewSet)
router.register(
    r"ai_non_predetermined_service_animal", AInonPredeterminedServiceAnimalViewSet
)
router.register(r"ai_predetermined_service_animal", AIPredeterminedServiceAnimalViewSet)
router.register(r"purchased_dosage", PurchasedDosageViewSet)
router.register(r"purchased_medicine", PurchasedMedicineViewSet)
router.register(r"locally_serviced_medicine", LocallyServicedMedicineViewSet)
router.register(r"locally_serviced_dosage", LocallyServicedDosageViewSet)
router.register(r"ai_predetermined_medicine", AIPredeterminedMedicineViewSet)
router.register(r"ai_predetermined_dosage", AIPredeterminedDosageViewSet)
router.register(r"ai_non_predetermined_medicine", AInonPredeterminedMedicineViewSet)
router.register(r"ai_non_predetermined_dosage", AInonPredeterminedDosageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
