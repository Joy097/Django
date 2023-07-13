from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name  = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
        
    def __str__(self):
        return self.name