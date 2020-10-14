from django.db import models
from django.urls import reverse
# Create your models here.



  


class Employee(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True )
    second_name = models.CharField(max_length=255, blank=True, null=True )
    user_name = models.CharField(max_length=500,  blank=True, null=True)
    email = models.CharField(max_length=500,  blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True )
    phone_number = models.IntegerField(default=0,  blank=True, null=True)
    country_code =models.IntegerField(default=0,  blank=True, null=True)
    specialization = models.CharField(max_length=255,  blank=True, null=True)
    gender =models.CharField(max_length=255,  blank=True, null=True)
    sample_essay = models.FileField( upload_to="Upload_files/%Y%m%d/" , max_length=255,  blank=True, null=True,)
    selfie = models.FileField( upload_to="Upload_files/%Y%m%d/" , max_length=255,  blank=True, null=True,)

    