from rest_framework import serializers
from .models import ContactRequest , VolunteeringApplication , VolunteeringOpportunity

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