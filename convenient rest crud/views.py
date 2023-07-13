from django.shortcuts import render
from .models import UserInfo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def UserList(request):
    
    if request.method == 'GET':
        entity = UserInfo.objects.all()
        serialized = UserSerializer(entity, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    
    if request.method == 'POST':
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)





@api_view(['GET', 'PUT', 'DELETE'])
def User_interact(request,pk):
    
    try:
        entities = UserInfo.objects.get(pk=pk)
    except UserInfo.DoesNotExist:
        return Response('Could not find',status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialized = UserSerializer(entities)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    
    if request.method == 'PUT':
        serialized = UserSerializer(entities,data=request.data)
        if serialized.is_valid():
            serialized.save() 
        return Response('Successfully updated',status = status.HTTP_202_ACCEPTED)
    
    if request.method == 'DELETE':
        entities.delete()
        return Response('Successfully deleted',status = status.HTTP_204_NO_CONTENT)
    