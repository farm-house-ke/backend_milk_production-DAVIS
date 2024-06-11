"""serializer for animal app"""

# serializers.py
from rest_framework import serializers
from .models import (
    Animal,
    Purchased,
    LocallyServiced,
    AIPredeterminedServiced,
    AInotPredeterminedServiced,
)


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = (
            "id",
            "name",
            "breed",
            "gender",
            "date_of_next_service",
        )


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
