from rest_framework.decorators import api_view
from api.models import Item
from api.serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


@api_view(['GET'])
def getItems(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getItem(request, pk):
    item = Item.objects.get(_id=pk)
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postItem(request):
    item = JSONParser().parse(request)
    item_serializer = ItemSerializer(data=item)
    if item_serializer.is_valid():
        item_serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
def putItem(request, pk):
    item = JSONParser().parse(request)
    item_data = Item.objects.get(_id=pk)
    item_serializer = ItemSerializer(item_data, data=item)
    if item_serializer.is_valid():
        item_serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
def deleteItem(request, pk):
    item = Item.objects.get(_id=pk)
    item.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False) 