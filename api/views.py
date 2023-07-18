from rest_framework.response import Response
from rest_framework.decorators import api_view
from store.models import Category, Category
from .serializers import CatSerializer
from rest_framework import status
import json

@api_view(['GET'])
def getcatData(request):
    items = Category.objects.all()
    serializer = CatSerializer(items, many=True)
    with open('cat.json', 'w') as file:
        json.dump(serializer.data, file)
    return Response(serializer.data)



@api_view(['GET'])
def getonecatData(request,pk):
    items = Category.objects.get(pk=pk)
    serializer = CatSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addcatData(request):
    serializer = CatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

@api_view(['DELETE'])
def removecat(request,pk):
    snippet = Category.objects.get(pk=pk)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def updatecat(request,pk):
    snippet = Category.objects.get(pk=pk)
    serializer = CatSerializer(snippet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)