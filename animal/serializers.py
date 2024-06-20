"""serializer for animal app"""

# serializers.py
from rest_framework import serializers
from .models import (
    Animal,
    Purchased,
    LocallyServiced,
    AIPredeterminedServiced,
    AInotPredeterminedServiced,
    TreatmentRecords,
    MedicineTreatment,
    Dosagetreatment,
)


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = (
            "name",
            "breed",
            "gender",
            "date_of_next_service",
            "source",
        )

        def create(self, validated_data):
            animal = Animal.objects.create(**validated_data)
            if validated_data["source"] == "purchased":
                Purchased.objects.create(animal=animal)
            elif validated_data["source"] == "locally_serviced":
                LocallyServiced.objects.create(animal=animal)
            elif validated_data["source"] == "ai_predetermined":
                AIPredeterminedServiced.objects.create(animal=animal)
            elif validated_data["source"] == "ai_not_predetermined":
                AInotPredeterminedServiced.objects.create(animal=animal)

            return animal


class PurchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchased
        fields = (
            "animal",
            "seller_name",
            "date_purchased",
        )


class LocallyServicedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocallyServiced
        fields = ("animal", "name_of_owner", "date_of_service", "birth_date")


class AIPredeterminedServicedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIPredeterminedServiced
        fields = (
            "animal",
            "date_of_service",
            "birth_date",
            "gender",
            "date_of_next_service",
        )


class AInotPredeterminedServicedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AInotPredeterminedServiced
        fields = (
            "animal",
            "date_of_service",
            "birth_date",
        )


class TreatmentRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = TreatmentRecords
        fields = (
            "animal",
            "date_of_diagnosis",
        )


class MedicineTreatmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicineTreatment
        fields = (
            "animal",
            "name_of_vet",
            "date_of_medicine_treatment",
            "current_state",
            "cured",
        )


class DosageTreatmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dosagetreatment
        fields = (
            "animal",
            "name_of_vet",
            "date_of_medicine_treatment",
            "dosage_treatment_used",
            "current_state",
            "cured",
        )
