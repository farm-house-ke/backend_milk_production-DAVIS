"""serializer for animal models."""

from rest_framework import serializers
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServiceAnimal,
)

class PurchasedAnimalSerializer(serializers.ModelSerializer):
    """serializer for purchased animal model."""

    class Meta:
        model = PurchasedAnimal
        fields = (
            "__all__"
        )


class LocallyServicedAnimalSerializer(serializers.ModelSerializer):
    """serializer for locally serviced animal."""
    class Meta:
        model = LocallyServicedAnimal
        fields = (
            "__all__"
        )


class AIPredeterminedServicedAnimalSerializer(serializers.ModelSerializer):
    """serializer for ai predetermined serviced animal."""

    class Meta:
        model = AIPredeterminedServiceAnimal
        fields = (
            "animal_name",
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
            "animal_name",
            "image",
            "breed",
            "gender",
            "date_of_next_service",
            "date_of_service",
            "birth_date",
        )
