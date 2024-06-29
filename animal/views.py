"""views for serializer models."""

from rest_framework.response import Response

from rest_framework import viewsets
from .serializers import (
    AnimalSerialializer,
    PurchasedAnimalSerializer,
    LocallyServicedAnimalSerializer,
    AIPredeterminedServicedAnimalSerializer,
    AInonPredeterminedServicedAnimalSerializer,
    MedicineTreatmentSerializer,
    DosageTreatmentSerializer,
)
from .models import (
    Animal,
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServiceAnimal,
    MedicineTreatment,
    Dosagetreatment,
)


class AnimalViewSet(viewsets.ModelViewSet):
    """view for animal model."""

    queryset = Animal.objects.all()
    serializer_class = AnimalSerialializer


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


class MedicineTreatmentViewSet(viewsets.ModelViewSet):
    """view for medicine report for animal model."""

    queryset = MedicineTreatment.objects.all()
    serializer_class = MedicineTreatmentSerializer


class DosageTreatmentViewSet(viewsets.ModelViewSet):
    """view for dosage report for animal model."""

    queryset = Dosagetreatment.objects.all()
    serializer_class = DosageTreatmentSerializer
