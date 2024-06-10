"""serializer for animal app"""
# serializers.py
from rest_framework import serializers
from.models import Animal, Purchased, LocallyServiced, AIPredeterminedServiced, AInotPredeterminedServiced

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class PurchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchased
        fields = '__all__'

class LocallyServicedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocallyServiced
        fields = '__all__'

class AIPredeterminedServicedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIPredeterminedServiced
        fields = '__all__'

class AInotPredeterminedServicedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AInotPredeterminedServiced
        fields = '__all__'
