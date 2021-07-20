from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class contact(models.Model):
    SNo= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField()
    datetime=models.DateTimeField(auto_now_add=True,blank=True)