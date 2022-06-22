from rest_framework import serializers
from .models import Item , ContactRequest , VolunteeringApplication , VolunteeringOpportunity

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = '__all__'
        
        
class VolunteeringOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteeringOpportunity
        fields = '__all__'
        
        
class VolunteeringApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteeringApplication
        fields = '__all__'