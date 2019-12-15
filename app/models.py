from django.db import models

# Create your models here.
class Vehicle(models.Model):
   
    vehicle_number=models.CharField(max_length=10)
    vehicle_insurance=models.FileField(upload_to='d/')
    created_at=models.DateTimeField(auto_now_add=True ,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)