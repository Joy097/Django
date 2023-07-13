from django.shortcuts import render
from .models import UserInfo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.

@api_view(['GET'])
def get_user(request):
    entities = UserInfo.objects.all()
    serialized = UserSerializer(entities, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request,pk):
    entities = UserInfo.objects.get(pk=pk)
    serialized = UserSerializer(entities)
    return Response(serialized.data, status=status.HTTP_200_OK)
     
@api_view(['POST'])
def create_user(request):
    serialized = UserSerializer(data = request.data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data, status=status.HTTP_201_CREATED)
        
@api_view(['DELETE'])
def delete_user(request,pk):
    entity = UserInfo.objects.get(pk=pk)
    entity.delete()
    return Response('Successfully deleted',status = status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_user(request, pk):
    entity = UserInfo.objects.get(pk=pk)
    serialized = UserSerializer(entity, data = request.data)
    if serialized.is_valid():
        serialized.save()
    return Response('Successfully updated',status = status.HTTP_202_ACCEPTED)
