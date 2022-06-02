from django.db import models
from rest_framework import serializers


# Create your models here.

class Cars(models.Model):

    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name

