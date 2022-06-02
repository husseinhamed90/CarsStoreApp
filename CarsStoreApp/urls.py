from django.urls import path
from CarsStoreApp import views

urlpatterns = [
    path("FetchAllStudents/", views.CarsStoreApiMethods.getAllCars, ),
]
