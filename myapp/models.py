from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=20,null=True,blank=True)
    phoneno=models.CharField(max_length=20,null=True,blank=True)
    profileimg=models.FileField(upload_to='images',null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    
class Rating(models.Model):
    rat=models.CharField( max_length=50,null=True,blank=True)