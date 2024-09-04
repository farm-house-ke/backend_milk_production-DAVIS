from rest_framework import serializers
from .models import (
    PurchasedAnimal,
    LocallyServicedAnimal,
    MedicineTreatment,
    DosageTreatment,
    AnimalBase,
    # Servicing,
    Disposal,
)


class AnimalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBase
        fields = "__all__"


# class ServicingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Servicing
#         fields = "__all__"


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


# class MilkProductionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MilkProduction
#         fields = "__all__"

#     def get_total_daily_quantity(self, obj):
#         return obj.morning_quantity + obj.evening_quantity
