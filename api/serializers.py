from rest_framework import serializers
from .models import Location, Place, Tourist


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
