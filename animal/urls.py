"""urls for animal app."""

from django.urls import path
from .views import (
    AnimalViewSet,
    PurchasedViewSet,
    LocallyServicedViewSet,
    AIPredeterminedServicedViewSet,
    AInotPredeterminedServicedViewSet,
    MedicineTreatmentViewSet,
    DosagetreatmentViewSet,
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
    path("purchased/", PurchasedViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "purchased/<int:pk>/",
        PurchasedViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "locally_serviced/",
        LocallyServicedViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "locally_serviced/<int:pk>/",
        LocallyServicedViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "ai_predetermined/",
        AIPredeterminedServicedViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_predetermined/<int:pk>/",
        AIPredeterminedServicedViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "ai_non_predetermined/",
        AInotPredeterminedServicedViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_non_predetermined/<int:pk>/",
        AInotPredeterminedServicedViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "medicinetreatment/",
        MedicineTreatmentViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "medicinetreatment/<int:pk>/",
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
        "dosagetreatment/",
        DosagetreatmentViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "dosagetreatment/<int:pk>/",
        DosagetreatmentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
