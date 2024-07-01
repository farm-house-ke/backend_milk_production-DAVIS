"""urls for animal app."""

from django.urls import path
from .views import (
    PurchasedAnimalViewSet,
    LocallyServicedAnimalViewSet,
    AIPredeterminedAndNonPredeterminedAnimalViewSet,
)

urlpatterns = [
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
        AIPredeterminedAndNonPredeterminedAnimalViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ai_predetermined_animal/<int:pk>/",
        AIPredeterminedAndNonPredeterminedAnimalViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
