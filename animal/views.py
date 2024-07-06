"""views for serializer models."""

# from rest_framework.response import Response

from rest_framework import viewsets
from .serializers import (
    PurchasedAnimalSerializer,
    LocallyServicedAnimalSerializer,
    AIPredeterminedServiceAnimalSerializer,
    AInonPredeterminedServiceAnimalSerializer,
)
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServicedAnimal,
)


class PurchasedAnimalViewSet(viewsets.ModelViewSet):
    """view for purchased animal."""

    queryset = PurchasedAnimal.objects.all()
    serializer_class = PurchasedAnimalSerializer


class LocallyServicedAnimalViewSet(viewsets.ModelViewSet):
    """view for locally serviced animal."""

    queryset = LocallyServicedAnimal.objects.all()
    serializer_class = LocallyServicedAnimalSerializer


class AIPredeterminedServiceAnimalViewSet(viewsets.ModelViewSet):
    """view for AI predetermined serviced animal."""

    queryset = AIPredeterminedServiceAnimal.objects.all()
    serializer_class = AIPredeterminedServiceAnimalSerializer


class AInonPredeterminedServiceAnimalViewSet(viewsets.ModelViewSet):
    """view for AI non predetermined serviced animal."""

    queryset = AInonPredeterminedServicedAnimal.objects.all()
    serializer_class = AInonPredeterminedServiceAnimalSerializer
