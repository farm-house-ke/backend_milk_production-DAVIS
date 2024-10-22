from rest_framework import serializers
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    MedicineTreatment,
    DosageTreatment,
    AnimalBase,
    Disposal,
    ServingBase,
    Bull,
    ArtificialInsemination,
)

class ServingBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServingBase
        fields = "__all__"

class BullServingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bull
        fields = "__all__"

class AISerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtificialInsemination
        fields = "__all__"


class AnimalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBase
        fields = "__all__"



class PurchasedAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedAnimal
        fields = "__all__"


class LocallyServicedAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocallyServicedAnimal
        fields = "__all__"


class MedicineTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineTreatment
        fields = "__all__"


class DosageTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageTreatment
        fields = "__all__"


class DisposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disposal
        fields = "__all__"