from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from .models import Product
from .serializers import pserializer

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = pserializer

class Product(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = pserializer
    lookup_field = 'pk'

