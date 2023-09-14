from django.db import models

# Create your models here.

class Company (models.Model):
    logo = models.ImageField('logo/')
    call_us = models.CharField(max_length=20)
    adreese = models.CharField(max_length=100)
    emial_us = models.CharField(max_length=50)
    facebook_link = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    discord_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200,null=True,blank=True)