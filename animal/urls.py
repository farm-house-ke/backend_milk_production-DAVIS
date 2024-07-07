"""urls for animal app."""

from django.urls import path
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

urlpatterns = [
    path(
        "ai_non_predetermined_medicine/",
        AInonPredeterminedMedicineViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_non_predetermined_medicine/<int:pk>/",
        AInonPredeterminedMedicineViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "purchased_medicine/",
        PurchasedMedicineViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "purchased_medicine/<int:pk>/",
        PurchasedMedicineViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "purchased_dosage/",
        PurchasedDosageViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "purchased_dosage/<int:pk>/",
        PurchasedDosageViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "locally_serviced_medicine/",
        LocallyServicedMedicineViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "locally_serviced_medicine/<int:pk>/",
        LocallyServicedMedicineViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "locally_serviced_dosage/",
        LocallyServicedDosageViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "locally_serviced_dosage/<int:pk>/",
        LocallyServicedDosageViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "ai_predetermined_medicine/",
        AIPredeterminedMedicineViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_predetermined_medicine/<int:pk>/",
        AIPredeterminedMedicineViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "ai_predetermined_dosage/",
        AIPredeterminedDosageViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_predetermined_dosage/<int:pk>/",
        AIPredeterminedDosageViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "ai_non_predetermined_dosage/",
        AInonPredeterminedDosageViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_non_predetermined_dosage/<int:pk>/",
        AInonPredeterminedDosageViewSet.as_view(
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
        "ai_predetermined_service_animal/",
        AIPredeterminedServiceAnimalViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_predetermined_service_animal/<int:pk>/",
        AIPredeterminedServiceAnimalViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "ai_non_predetermined_service_animal/",
        AInonPredeterminedServiceAnimalViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
    ),
    path(
        "ai_non_predetermined_service_animal/<int:pk>/",
        AInonPredeterminedServiceAnimalViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
