"""urls for animal app."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PurchasedViewSet,
    LocallyServicedViewSet,
    AIPredeterminedViewSet,
    AInonPredeterminedViewSet,
    MedicineTreatmentViewSet,
    DosageTreatmentViewSet
)

router = DefaultRouter()
router.register(r"purchased_animal", PurchasedViewSet)
router.register(r"locally_serviced_animal", LocallyServicedViewSet)
router.register(
    r"ai_non_predetermined_service_animal", AInonPredeterminedViewSet
)
router.register(r"ai_predetermined_service_animal", AIPredeterminedViewSet)
router.register(r"dosage", DosageTreatmentViewSet)
router.register(r"medicine", MedicineTreatmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
