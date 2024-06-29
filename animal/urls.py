"""urls for animal app."""

from django.urls import path
from .views import (
    AnimalViewSet,
    PurchasedAnimalViewSet,
    LocallyServicedAnimalViewSet,
    AIPredeterminedAnimalViewSet,
    AInonPredeterminedAnimalViewSet,
    MedicineTreatmentViewSet,
    DosageTreatmentViewSet,
)

urlpatterns = [
    path("animals/", AnimalViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "animals/<int:pk>/",
        AnimalViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "purchased_animal/",
        PurchasedAnimalViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "purchased_animal/<int:pk>/",
        PurchasedAnimalViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "locally_serviced_animal/",
        LocallyServicedAnimalViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "locally_serviced_animal/<int:pk>/",
        LocallyServicedAnimalViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "ai_predetermined_animal/",
        AIPredeterminedAnimalViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_predetermined_animal/<int:pk>/",
        AIPredeterminedAnimalViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "ai_non_predetermined_animal/",
        AInonPredeterminedAnimalViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_non_predetermined_animal/<int:pk>/",
        AInonPredeterminedAnimalViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "medicine_treatment/",
        MedicineTreatmentViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "medicine_treatment/<int:pk>/",
        MedicineTreatmentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "dosage_treatment/",
        DosageTreatmentViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "dosage_treatment/<int:pk>/",
        DosageTreatmentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
