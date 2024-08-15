"""views for serializer models."""
from django.http import JsonResponse
from django.db import models
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from .serializers import (
    AnimalBaseSerializer,
    PurchasedAnimalSerializer,
    LocallyServicedAnimalSerializer,
    AIPredeterminedServiceAnimalSerializer,
    AInonPredeterminedServicedAnimalSerializer,
    MedicineTreatmentSerializer,
    DosageTreatmentSerializer,
)
from .models import (
    AnimalBase,
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

class AnimalBaseViewSet(viewsets.ModelViewSet):
    queryset = AnimalBase.objects.all()
    serializer_class = AnimalBaseSerializer


class GenderDistributionView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            gender_counts = AnimalBase.objects.values("gender").annotate(
                count=Count("gender")
            )
            data = {"male": 0, "female": 0}
            for entry in gender_counts:
                if entry["gender"] == "M":
                    data["male"] = entry["count"]
                elif entry["gender"] == "F":
                    data["female"] = entry["count"]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
