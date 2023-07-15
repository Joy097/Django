from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category
from .serializers import pserializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getproducts(request):
    snippet = Product.objects.all()
    serialized = pserializer(snippet, many=True)
    return Response(serialized.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def postproducts(request):
    serialized = pserializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data,status=status.HTTP_201_CREATED)
    return Response('Please provide a valid data')

@api_view(['PUT'])
def putproducts(request,pk):
    snippet = Product.objects.get(pk=pk)
    serialized = pserializer(snippet, data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data,status=status.HTTP_202_ACCEPTED)
    return Response('Please provide a valid data')

@api_view(['DELETE'])
def delproducts(request,pk):
    snippet = Product.objects.get(pk=pk)
    snippet.delete()
    return Response('Successfully Deleted',status=status.HTTP_410_GONE)
    