"""views for serializer models."""

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import viewsets
from .serializers import (
    PurchasedAnimalSerializer,
    LocallyServicedAnimalSerializer,
    AIPredeterminedServiceAnimalSerializer,
    AInonPredeterminedServiceAnimalSerializer,
    PurchasedDosageSerializer,
    PurchasedMedicineSerializer,
    LocallyServicedDosageSerializer,
    LocallyServicedMedicineSerializer,
    AIPredeterminedDosageSerializer,
    AIPredeterminedMedicineSerializer,
    AInonPredeterminedDosageSerializer,
    AInonPredeterminedMedicineSerializer,
)
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServicedAnimal,
    PurchasedDosageTreatment,
    PurchasedMedicineTreatment,
    LocallyServicedDosageTreatment,
    LocallyServicedMedicineTreatment,
    AIPredeterminedDosageTreatment,
    AIPredeterminedMedicineTreatment,
    AInonPredeterminedMedicineTreatment,
    AInonPredeterminedDosageTreatment,
)


class PurchasedAnimalViewSet(viewsets.ModelViewSet):
    """view for purchased animal."""

    queryset = PurchasedAnimal.objects.all()
    serializer_class = PurchasedAnimalSerializer

class PurchasedDosageViewSet(viewsets.ModelViewSet):
    """view for purchased dosage report."""

    queryset = PurchasedDosageTreatment.objects.all()
    serializer_class = PurchasedDosageSerializer


class PurchasedMedicineViewSet(viewsets.ModelViewSet):
    """view for purchased medicine report."""

    queryset = PurchasedMedicineTreatment.objects.all()
    serializer_class = PurchasedMedicineSerializer


class LocallyServicedAnimalViewSet(viewsets.ModelViewSet):
    """view for locally serviced animal."""

    queryset = LocallyServicedAnimal.objects.all()
    serializer_class = LocallyServicedAnimalSerializer


class LocallyServicedMedicineViewSet(viewsets.ModelViewSet):
    """view for locally serviced medicine report."""

    queryset = LocallyServicedMedicineTreatment.objects.all()
    serializer_class = LocallyServicedMedicineSerializer


class LocallyServicedDosageViewSet(viewsets.ModelViewSet):
    """view for locally serviced dosage report."""

    queryset = LocallyServicedDosageTreatment.objects.all()
    serializer_class = LocallyServicedDosageSerializer


class AIPredeterminedServiceAnimalViewSet(viewsets.ModelViewSet):
    """view for AI predetermined serviced animal."""

    queryset = AIPredeterminedServiceAnimal.objects.all()
    serializer_class = AIPredeterminedServiceAnimalSerializer


class AIPredeterminedMedicineViewSet(viewsets.ModelViewSet):
    """view for ai predetermined serviced medicine report."""

    queryset = AIPredeterminedMedicineTreatment.objects.all()
    serializer_class = AIPredeterminedMedicineSerializer


class AIPredeterminedDosageViewSet(viewsets.ModelViewSet):
    """view for ai predetermined serviced dosage report."""

    queryset = AIPredeterminedDosageTreatment.objects.all()
    serializer_class = AIPredeterminedDosageSerializer


class AInonPredeterminedServiceAnimalViewSet(viewsets.ModelViewSet):
    """view for AI non predetermined serviced animal."""

    queryset = AInonPredeterminedServicedAnimal.objects.all()
    serializer_class = AInonPredeterminedServiceAnimalSerializer


class AInonPredeterminedMedicineViewSet(viewsets.ModelViewSet):
    """view for ai non predetermined serviced medicine report."""

    queryset = AInonPredeterminedMedicineTreatment.objects.all()
    serializer_class = AInonPredeterminedMedicineSerializer


class AInonPredeterminedDosageViewSet(viewsets.ModelViewSet):
    """view for ai non predetermined serviced dosage report."""

    queryset = AInonPredeterminedDosageTreatment.objects.all()
    serializer_class = AInonPredeterminedDosageSerializer
