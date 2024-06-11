"""views for animal app."""

# views.py
from rest_framework import viewsets
from .models import (
    Animal,
    Purchased,
    LocallyServiced,
    AInotPredeterminedServiced,
    AIPredeterminedServiced,
)
from .serializers import (
    AnimalSerializer,
    PurchasedSerializer,
    LocallyServicedSerializer,
    AIPredeterminedServicedSerializer,
    AInotPredeterminedServicedSerializer,
)


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class PurchasedViewSet(viewsets.ModelViewSet):
    queryset = Purchased.objects.all()
    serializer_class = PurchasedSerializer


class LocallyServicedViewSet(viewsets.ModelViewSet):
    queryset = LocallyServiced.objects.all()
    serializer_class = LocallyServicedSerializer


class AIPredeterminedServicedViewSet(viewsets.ModelViewSet):
    queryset = AIPredeterminedServiced.objects.all()
    serializer_class = AIPredeterminedServicedSerializer


class AInotPredeterminedServicedViewSet(viewsets.ModelViewSet):
    queryset = AInotPredeterminedServiced.objects.all()
    serializer_class = AInotPredeterminedServicedSerializer
