from rest_framework.decorators import api_view
from api.models import Tourist
from api.serializers import TouristSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


@api_view(['GET'])
def getTourists(request):
    Tourists = Tourist.objects.all()
    serializer = TouristSerializer(Tourists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTourist(request, pk):
    Tourist = Tourist.objects.get(_id=pk)
    serializer = TouristSerializer(Tourist, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postTourist(request):
    Tourist = JSONParser().parse(request)
    serializer = TouristSerializer(data=Tourist)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)


@api_view(['PUT'])
def putTourist(request, pk):
    Tourist = JSONParser().parse(request)
    Tourist_data = Tourist.objects.get(_id=pk)
    serializer = TouristSerializer(Tourist_data, data=Tourist)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)


@api_view(['DELETE'])
def deleteTourist(request, pk):
    Tourist = Tourist.objects.get(_id=pk)
    Tourist.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False)
