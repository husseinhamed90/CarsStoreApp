from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Car, Brand, CarModel


class CarJson(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class brandJson(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ModelJson(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class userJson(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "first_name", "last_name")
