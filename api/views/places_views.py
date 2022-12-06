from rest_framework.decorators import api_view
from api.models import Place
from api.serializers import PlaceSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


@api_view(['GET'])
def getPlaces(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPlace(request, pk):
    place = Place.objects.get(_id=pk)
    serializer = PlaceSerializer(place, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def getAllPlaces(request):
    return Response({"payload": ["Qadisha Valley","Gebran Museum","Al-Arez","River Rock Restaurant","Hotel Chbat", "La Maison des Cedres"]})


@api_view(['POST'])
def postPlace(request):
    place = JSONParser().parse(request)
    serializer = PlaceSerializer(data=place)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)


@api_view(['PUT'])
def putPlace(request, pk):
    place = JSONParser().parse(request)
    Place_data = Place.objects.get(_id=pk)
    serializer = PlaceSerializer(
        Place_data, data=place)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)


@api_view(['DELETE'])
def deletePlace(request, pk):
    place = Place.objects.get(_id=pk)
    place.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False)
