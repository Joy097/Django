from rest_framework import generics
from .models import Product
from .serializers import pserializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = pserializer

class Product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = pserializer
    lookup_field = 'pk'

