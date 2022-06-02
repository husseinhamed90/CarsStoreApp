from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Cars


class studentJson(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class userJson(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "first_name", "last_name")
