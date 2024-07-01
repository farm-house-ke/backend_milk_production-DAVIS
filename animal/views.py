"""views for serializer models."""

# from rest_framework.response import Response

from rest_framework import viewsets
from .serializers import (
    PurchasedAnimalSerializer,
    LocallyServicedAnimalSerializer,
    AIPredeterminedAndNonPredeterminedServicedAnimalSerializer,
)
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedAndNonPredeterminedServiceAnimal,

)


class PurchasedAnimalViewSet(viewsets.ModelViewSet):
    """view for purchased animal."""

    queryset = PurchasedAnimal.objects.all()
    serializer_class = PurchasedAnimalSerializer


class LocallyServicedAnimalViewSet(viewsets.ModelViewSet):
    """view for locally serviced animal."""

    queryset = LocallyServicedAnimal.objects.all()
    serializer_class = LocallyServicedAnimalSerializer


class AIPredeterminedAndNonPredeterminedAnimalViewSet(viewsets.ModelViewSet):
    """view for ai predetermined animal."""

    queryset = AIPredeterminedAndNonPredeterminedServiceAnimal.objects.all()
    serializer_class = AIPredeterminedAndNonPredeterminedServicedAnimalSerializer
