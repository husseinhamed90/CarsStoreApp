from django.db import models
from rest_framework import serializers


# Create your models here.

class Brand(models.Model):
    BrandName = models.CharField(max_length=100)

    def __str__(self):
        return self.BrandName


class CarModel(models.Model):
    BrandID = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    ModelName = models.CharField(max_length=100)

    def __str__(self):
        return self.ModelName


class Car(models.Model):
    BrandID = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    ModelID = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True)
    carName = models.CharField(max_length=100)
    carImage = models.CharField(max_length=100)
    carPrice = models.IntegerField()
    hours = models.IntegerField()
    modelYear = models.IntegerField()

    def __str__(self):
        return self.carName
