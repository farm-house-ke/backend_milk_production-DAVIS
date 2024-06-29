"""serializer for animal models."""

from rest_framework import serializers
from .models import (
    Animal,
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServiceAnimal,
    MedicineTreatment,
    Dosagetreatment,
)


class AnimalSerialializer(serializers.ModelSerializer):
    """serializer for animal model"""

    class Meta:
        model = Animal
        fields = "__all__"


class PurchasedAnimalSerializer(serializers.ModelSerializer):
    """serializer for purchased animal model."""

    class Meta:
        model = PurchasedAnimal
        fields = (
            "animal",
            "image",
            "breed",
            "gender",
            "date_of_next_service",
            "seller_name",
            "date_purchased",
        )


class LocallyServicedAnimalSerializer(serializers.ModelSerializer):
    """serializer for locally serviced animal."""

    class Meta:
        model = LocallyServicedAnimal
        fields = (
            "animal",
            "image",
            "breed",
            "gender",
            "date_of_next_service",
            "name_of_owner",
            "date_of_service",
            "birth_date",
        )


class AIPredeterminedServicedAnimalSerializer(serializers.ModelSerializer):
    """serializer for ai predetermined serviced animal."""

    class Meta:
        model = AIPredeterminedServiceAnimal
        fields = (
            "animal",
            "image",
            "breed",
            "gender",
            "date_of_next_service",
            "date_of_service",
            "birth_date",
        )


class AInonPredeterminedServicedAnimalSerializer(serializers.ModelSerializer):
    """serializer for ai non predetermined serviced animal."""

    class Meta:
        model = AInonPredeterminedServiceAnimal
        fields = (
            "animal",
            "image",
            "breed",
            "gender",
            "date_of_next_service",
            "date_of_service",
            "birth_date",
        )


class MedicineTreatmentSerializer(serializers.ModelSerializer):
    """serializer for medicine treatment report for animal model."""

    class Meta:
        model = MedicineTreatment
        fields = (
            "animal",
            "date_of_diagnosis",
            "name_of_vet",
            "date_of_medicine_treatment",
            "current_state",
            "cured",
        )


class DosageTreatmentSerializer(serializers.ModelSerializer):
    """serializer for dosage treatment report for animal model."""

    class Meta:
        model = Dosagetreatment
        fields = (
            "animal",
            "date_of_diagnosis",
            "name_of_vet",
            "date_of_medicine_treatment",
            "dosage_treatment_used",
            "current_state",
            "cured",
        )
