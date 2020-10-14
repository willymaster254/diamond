from django.db import models
from django.shortcuts import reverse
from django import forms


# Create your models here.
from django.db import models

class Orders(models.Model):
    topic = models.CharField(max_length=255, blank=True, null=True )
    pages = models.IntegerField(default=0,  blank=True, null=True)
    style = models.CharField(max_length=255,  blank=True, null=True)
    subject = models.CharField(max_length=500,  blank=True, null=True)
    amount = models.IntegerField(default=0.0, blank=True, null=True)
    instructions = models.TextField(max_length=5000,  blank=True, null=True)
    uploads = models.FileField( upload_to="Upload_files/%Y%m%d/" , max_length=255,  blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True,  blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,  )

    def get_absolute_url(self):
        return reverse('accounts:order')

class UploadFiles(models.Model):
    files = models.FileField(upload_to = "Upload_files/%Y%m%d/" , max_length=255,  blank=True, null=True )
    
















