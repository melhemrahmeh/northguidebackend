from rest_framework import serializers
from .models import Items , ContactRequests , VolunteeringApplications , VolunteeringOpportunities

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequests
        fields = '__all__'
        
        
class VolunteeringOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteeringOpportunities
        fields = '__all__'
        
        
class VolunteeringApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteeringApplications
        fields = '__all__'