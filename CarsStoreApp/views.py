from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .json import CarJson, userJson, ModelJson, brandJson
from .models import Car, CarModel, Brand
from . import models
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def gotoHomePage(request):
    return render(request, "index.html")


def insert(n1, n2, ):
    newstudent = models.student(name=n1, age=n2)
    newstudent.save()
    return HttpResponse(n1 + " inserted")


def update(n1, n2, stud_id):
    updatedstudent = models.student(id=stud_id, name=n1, age=n2)
    updatedstudent.save()
    return HttpResponse(n1 + " updated")


def delete(stud_id):
    deletedstudent = models.student(id=stud_id)
    deletedstudent.delete()
    return HttpResponse(str(stud_id) + " deleted")


def showAll():
    data = models.student.objects.order_by('age')
    return HttpResponse(str(data[0]))


# -----------------------------------------------------------------------------------------------------------------#


class CarsStoreApiMethods:

    @api_view(['GET'])
    def getCarById(self):
        try:
            carObject = Car.objects.get(id=self.data['id'])
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CarJson(carObject)
        return Response(serializer.data)

    @api_view(['GET'])
    def getAllCars(self):
        objects = Car.objects.all()
        jsonOfObjects = CarJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['POST'])
    def getFilteredCarByBrandID(self):
        print(self.data)
        objects = Car.objects.filter(BrandID=self.data['BrandID'])
        jsonOfObjects = CarJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['POST'])
    def getFilteredCarByModelID(self):
        if self.data['modelYear'] is not None:
            objects = Car.objects.filter(ModelID=self.data['ModelID'], modelYear=self.data['modelYear'])
        else:
            objects = Car.objects.filter(ModelID=self.data['ModelID'])
        jsonOfObjects = CarJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['POST'])
    def getFilteredModels(self):
        print(self.data)
        objects = CarModel.objects.filter(BrandID=self.data['BrandID'])
        jsonOfObjects = ModelJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['POST'])
    def getFilteredCars(self):
        print(self.data)
        objects = Car.objects.filter(BrandID=self.data['BrandID'], ModelID=self.data['ModelID'])
        jsonOfObjects = CarJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['GET'])
    def getAllBrands(self):
        objects = Brand.objects.all()
        jsonOfObjects = brandJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['GET'])
    def getAllModels(self):
        objects = CarModel.objects.all()
        jsonOfObjects = ModelJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['GET'])
    def orderStudents(self):

        objects = Car.objects.order_by('age')
        jsonOfObjects = CarJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['GET'])
    def getStudentsGreaterThanSpecificAge(self, age):

        objects = Car.objects.filter(age__gt=age)
        jsonOfObjects = CarJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['POST'])
    def post(self):
        serializer = CarJson(data=self.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def getAllUsers(self):
        objects = User.objects.all()
        jsonOfObjects = userJson(objects, many=True)
        return Response(jsonOfObjects.data)

    @api_view(['POST'])
    def register(self):

        try:
            newUser = User.objects.create_user(username=self.data['username'], email=self.data['email'],
                                               password=self.data['password'], )
            newUser.first_name = self.data['first_name']
            newUser.last_name = self.data['last_name']
            self.data["id"] = newUser.id
            newUser.save()

        except User.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(self.data)

    @api_view(['POST'])
    def login(self):

        userObject = authenticate(username=self.data['username'], password=self.data['password'])
        if userObject is not None:
            login(self, userObject)
            self.data["result"] = "valid user"
            objects = User.objects.get(id=getattr(userObject, "id"))
            jsonOfObjects = userJson(objects)
            return Response(jsonOfObjects.data, status=status.HTTP_201_CREATED)
        return Response({"result": "invalid user"}, status=status.HTTP_400_BAD_REQUEST)
