from rest_framework.decorators import api_view
from api.models import ContactRequest
from api.serializers import ContactRequestSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


@api_view(['GET'])
def getContactRequests(request):
    contactRequests = ContactRequest.objects.all()
    serializer = ContactRequestSerializer(contactRequests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getContactRequest(request, pk):
    contactRequest = ContactRequest.objects.get(_id=pk)
    serializer = ContactRequestSerializer(contactRequest, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postContactRequest(request):
    contactRequest = JSONParser().parse(request)
    serializer = ContactRequestSerializer(data=contactRequest)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
def putContactRequest(request, pk):
    contactRequest = JSONParser().parse(request)
    contactRequest_data = ContactRequest.objects.get(_id=pk)
    serializer = ContactRequestSerializer(contactRequest_data, data=contactRequest)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
def deleteContactRequest(request, pk):
    contactRequest = ContactRequest.objects.get(_id=pk)
    contactRequest.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False) 