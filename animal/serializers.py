from rest_framework import serializers
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServicedAnimal,
    MedicineTreatment,
    DosageTreatment,
    AnimalBase,
)


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


class AIPredeterminedServiceAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIPredeterminedServiceAnimal
        fields = "__all__"


class AInonPredeterminedServicedAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AInonPredeterminedServicedAnimal
        fields = "__all__"


class MedicineTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineTreatment
        fields = "__all__"


class DosageTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageTreatment
        fields = "__all__"
