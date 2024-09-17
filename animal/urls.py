"""urls for animal app."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenderDistributionView,
    PurchasedViewSet,
    LocallyServicedViewSet,
    MedicineTreatmentViewSet,
    AnimalBaseViewSet,
    DosageTreatmentViewSet,
    DisposalViewSet,
)

router = DefaultRouter()
router.register(r"animal_base", AnimalBaseViewSet)
router.register(r"purchased_animal", PurchasedViewSet)
router.register(r"locally_serviced_animal", LocallyServicedViewSet)
router.register(r"dosage", DosageTreatmentViewSet)
router.register(r"medicine", MedicineTreatmentViewSet)
router.register(r"disposal", DisposalViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "gender-distribution/",
        GenderDistributionView.as_view(),
        name="gender_distribution",
    ),
]
