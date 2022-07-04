from rest_framework.decorators import api_view
from api.models import VolunteeringOpening
from api.serializers import VolunteeringOpportunitySerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


@api_view(['GET'])
def getVolunteeringOpportunities(request):
    volunteeringOpportunities = VolunteeringOpening.objects.all()
    serializer = VolunteeringOpportunitySerializer(volunteeringOpportunities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getVolunteeringOpportunity(request, pk):
    volunteeringOpportunity = VolunteeringOpening.objects.get(_id=pk)
    serializer = VolunteeringOpportunitySerializer(volunteeringOpportunity, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postVolunteeringOpportunity(request):
    volunteeringOpportunity = JSONParser().parse(request)
    serializer = VolunteeringOpportunitySerializer(data=volunteeringOpportunity)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
def putVolunteeringOpportunity(request, pk):
    volunteeringOpportunity = JSONParser().parse(request)
    volunteeringOpportunity_data = VolunteeringOpening.objects.get(_id=pk)
    serializer = VolunteeringOpportunitySerializer(volunteeringOpportunity_data, data=volunteeringOpportunity)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
def deleteVolunteeringOpportunity(request, pk):
    volunteeringOpportunity = VolunteeringOpening.objects.get(_id=pk)
    volunteeringOpportunity.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False)