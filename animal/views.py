"""views for serializer models."""

from rest_framework import viewsets
from .serializers import (
    PurchasedAnimalSerializer,
    LocallyServicedAnimalSerializer,
    AIPredeterminedServiceAnimalSerializer,
    AInonPredeterminedServicedAnimalSerializer,
    MedicineTreatmentSerializer,
    DosageTreatmentSerializer,
)
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServicedAnimal,
    MedicineTreatment,
    DosageTreatment,
)


class PurchasedViewSet(viewsets.ModelViewSet):
    queryset = PurchasedAnimal.objects.all()
    serializer_class = PurchasedAnimalSerializer


class LocallyServicedViewSet(viewsets.ModelViewSet):
    queryset = LocallyServicedAnimal.objects.all()
    serializer_class = LocallyServicedAnimalSerializer


class AIPredeterminedViewSet(viewsets.ModelViewSet):
    queryset = AIPredeterminedServiceAnimal.objects.all()
    serializer_class = AIPredeterminedServiceAnimalSerializer


class AInonPredeterminedViewSet(viewsets.ModelViewSet):
    queryset = AInonPredeterminedServicedAnimal.objects.all()
    serializer_class = AInonPredeterminedServicedAnimalSerializer


class MedicineTreatmentViewSet(viewsets.ModelViewSet):
    queryset = MedicineTreatment.objects.all()
    serializer_class = MedicineTreatmentSerializer


class DosageTreatmentViewSet(viewsets.ModelViewSet):
    queryset = DosageTreatment.objects.all()
    serializer_class = DosageTreatmentSerializer
