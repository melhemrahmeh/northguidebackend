from rest_framework.decorators import api_view
from api.models import Location
from api.serializers import LocationSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


@api_view(['GET'])
def getLocations(request):
    Locations = Location.objects.all()
    serializer = LocationSerializer(Locations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getLocation(request, pk):
    Location = Location.objects.get(_id=pk)
    serializer = LocationSerializer(Location, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postLocation(request):
    Location = JSONParser().parse(request)
    serializer = LocationSerializer(data=Location)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)


@api_view(['PUT'])
def putLocation(request, pk):
    Location = JSONParser().parse(request)
    Location_data = Location.objects.get(_id=pk)
    serializer = LocationSerializer(Location_data, data=Location)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)


@api_view(['DELETE'])
def deleteLocation(request, pk):
    Location = Location.objects.get(_id=pk)
    Location.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False)
