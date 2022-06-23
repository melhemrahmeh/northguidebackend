from rest_framework.decorators import api_view
from api.models import VolunteeringApplications
from api.serializers import VolunteeringApplicationSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


@api_view(['GET'])
def getVolunteeringApplications(request):
    volunteeringApplications = VolunteeringApplications.objects.all()
    serializer = VolunteeringApplicationSerializer(volunteeringApplications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getVolunteeringApplication(request, pk):
    volunteeringApplication = VolunteeringApplications.objects.get(_id=pk)
    serializer = VolunteeringApplicationSerializer(volunteeringApplication, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postVolunteeringApplication(request):
    volunteeringApplication = JSONParser().parse(request)
    serializer = VolunteeringApplicationSerializer(data=volunteeringApplication)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
def putVolunteeringApplication(request, pk):
    volunteeringApplication = JSONParser().parse(request)
    volunteeringApplication_data = VolunteeringApplications.objects.get(_id=pk)
    serializer = VolunteeringApplicationSerializer(volunteeringApplication_data, data=volunteeringApplication)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
def deleteVolunteeringApplication(request, pk):
    volunteeringApplication = VolunteeringApplications.objects.get(_id=pk)
    volunteeringApplication.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False) 