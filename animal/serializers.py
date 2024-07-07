"""serializer for animal models."""

from rest_framework import serializers
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    AIPredeterminedServiceAnimal,
    AInonPredeterminedServicedAnimal,
    PurchasedMedicineTreatment,
    PurchasedDosageTreatment,
    LocallyServicedDosageTreatment,
    LocallyServicedMedicineTreatment,
    AIPredeterminedDosageTreatment,
    AIPredeterminedMedicineTreatment,
    AInonPredeterminedDosageTreatment,
    AInonPredeterminedMedicineTreatment,
)


class PurchasedAnimalSerializer(serializers.ModelSerializer):
    """serializer for purchased animal model."""

    class Meta:
        model = PurchasedAnimal
        fields = "__all__"


class PurchasedMedicineSerializer(serializers.ModelSerializer):
    """class serializer for purchased medicine report."""

    class Meta:
        model = PurchasedMedicineTreatment
        fields = "__all__"


class PurchasedDosageSerializer(serializers.ModelSerializer):
    """class serializer for purchased dosage report."""

    class Meta:
        model = PurchasedDosageTreatment
        fields = "__all__"


class LocallyServicedAnimalSerializer(serializers.ModelSerializer):
    """serializer for locally serviced animal."""

    class Meta:
        model = LocallyServicedAnimal
        fields = "__all__"


class LocallyServicedMedicineSerializer(serializers.ModelSerializer):
    """class serializer for locally serviced medicine report."""

    class Meta:
        model = LocallyServicedMedicineTreatment
        fields = "__all__"


class LocallyServicedDosageSerializer(serializers.ModelSerializer):
    """class serializer for locally serviced dosage report."""

    class Meta:
        model = LocallyServicedDosageTreatment
        fields = "__all__"


class AIPredeterminedServiceAnimalSerializer(serializers.ModelSerializer):
    """serializer for ai predetermined serviced animal."""

    class Meta:
        model = AIPredeterminedServiceAnimal
        fields = "__all__"


class AIPredeterminedMedicineSerializer(serializers.ModelSerializer):
    """class serializer for ai predetermined medicine report."""

    class Meta:
        model = AIPredeterminedMedicineTreatment
        fields = "__all__"


class AIPredeterminedDosageSerializer(serializers.ModelSerializer):
    """class serialzer for ai predetermined dosage report."""

    class Meta:
        model = AIPredeterminedDosageTreatment
        fields = "__all__"


class AInonPredeterminedServiceAnimalSerializer(serializers.ModelSerializer):
    """serializer for ai non predetermined serviced animal."""

    class Meta:
        model = AInonPredeterminedServicedAnimal
        fields = "__all__"


class AInonPredeterminedMedicineSerializer(serializers.ModelSerializer):
    """class serializer for ai non predetermined medicine report."""

    class Meta:
        model = AInonPredeterminedMedicineTreatment
        fields = "__all__"


class AInonPredeterminedDosageSerializer(serializers.ModelSerializer):
    """class serializer for ai non predetermined dosage report."""

    class Meta:
        model = AInonPredeterminedDosageTreatment
        fields = "__all__"
