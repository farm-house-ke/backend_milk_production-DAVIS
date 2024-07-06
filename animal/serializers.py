"""serializer for animal models."""

from rest_framework import serializers
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServicedAnimal,
)


class PurchasedAnimalSerializer(serializers.ModelSerializer):
    """serializer for purchased animal model."""

    class Meta:
        model = PurchasedAnimal
        fields = "__all__"


class LocallyServicedAnimalSerializer(serializers.ModelSerializer):
    """serializer for locally serviced animal."""

    class Meta:
        model = LocallyServicedAnimal
        fields = "__all__"


class AIPredeterminedServiceAnimalSerializer(serializers.ModelSerializer):
    """serializer for ai predetermined serviced animal."""

    class Meta:
        model = AIPredeterminedServiceAnimal
        fields = "__all__"


class AInonPredeterminedServiceAnimalSerializer(serializers.ModelSerializer):
    """serializer for ai non predetermined serviced animal."""

    class Meta:
        model = AInonPredeterminedServicedAnimal
        fields = "__all__"
