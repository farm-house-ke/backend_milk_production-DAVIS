"""views for serializer models."""

# from rest_framework.response import Response

from rest_framework import viewsets
from .serializers import (
    PurchasedAnimalSerializer,
    LocallyServicedAnimalSerializer,
    AIPredeterminedServicedAnimalSerializer,
    AInonPredeterminedServicedAnimalSerializer,
)
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServiceAnimal,
)


class PurchasedAnimalViewSet(viewsets.ModelViewSet):
    """view for purchased animal."""

    queryset = PurchasedAnimal.objects.all()
    serializer_class = PurchasedAnimalSerializer


class LocallyServicedAnimalViewSet(viewsets.ModelViewSet):
    """view for locally serviced animal."""

    queryset = LocallyServicedAnimal.objects.all()
    serializer_class = LocallyServicedAnimalSerializer


class AIPredeterminedAnimalViewSet(viewsets.ModelViewSet):
    """view for ai predetermined animal."""

    queryset = AIPredeterminedServiceAnimal.objects.all()
    serializer_class = AIPredeterminedServicedAnimalSerializer


class AInonPredeterminedAnimalViewSet(viewsets.ModelViewSet):
    """view for ai non predetermined animal."""

    queryset = AInonPredeterminedServiceAnimal.objects.all()
    serializer_class = AInonPredeterminedServicedAnimalSerializer
