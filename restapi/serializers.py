from rest_framework import serializers
from .models import Product, Category

class pserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class cserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'