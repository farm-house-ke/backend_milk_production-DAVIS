"""views for serializer models."""

from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from .serializers import (
    AnimalBaseSerializer,
    PurchasedAnimalSerializer,
    LocallyServicedAnimalSerializer,
    MedicineTreatmentSerializer,
    DosageTreatmentSerializer,
    ServingBaseSerializer,
    BullServingSerializer,
    AISerializer,
    DisposalSerializer,

)
from .models import (
    AnimalBase,
    PurchasedAnimal,
    LocallyServicedAnimal,
    MedicineTreatment,
    DosageTreatment,
    ServingBase,
    Bull,
    ArtificialInsemination,
    Disposal,
)

class ServingBaseViewSet(viewsets.ModelViewSet):
    queryset = ServingBase.objects.all()
    serializer_class = ServingBaseSerializer

class BullViewSet(viewsets.ModelViewSet):
    queryset = Bull.objects.all()
    serializer_class = BullServingSerializer

class AIViewSet(viewsets.ModelViewSet):
    queryset = ArtificialInsemination.objects.all()
    serializer_class = AISerializer

class PurchasedViewSet(viewsets.ModelViewSet):
    queryset = PurchasedAnimal.objects.all()
    serializer_class = PurchasedAnimalSerializer


class LocallyServicedViewSet(viewsets.ModelViewSet):
    queryset = LocallyServicedAnimal.objects.all()
    serializer_class = LocallyServicedAnimalSerializer


class MedicineTreatmentViewSet(viewsets.ModelViewSet):
    queryset = MedicineTreatment.objects.all()
    serializer_class = MedicineTreatmentSerializer


class DosageTreatmentViewSet(viewsets.ModelViewSet):
    queryset = DosageTreatment.objects.all()
    serializer_class = DosageTreatmentSerializer


class AnimalBaseViewSet(viewsets.ModelViewSet):
    queryset = AnimalBase.objects.all()
    serializer_class = AnimalBaseSerializer

    def get_query(self):
        queryset = super().get_queryset()
        gender = self.request.query_params.get("gender")

        if gender:
            queryset = queryset.filter(gender=gender)
        return queryset


class DisposalViewSet(viewsets.ModelViewSet):
    queryset = Disposal.objects.all()
    serializer_class = DisposalSerializer

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
