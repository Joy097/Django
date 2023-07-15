from django.db import models

# Create your models here.

class Category(models.Model):
    name  = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    
    def __str__(self):
        return (f"{self.name}")
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f"{self.name}")