from django.urls import path
from CarsStoreApp import views

urlpatterns = [
    path("FetchAllCars/", views.CarsStoreApiMethods.getAllCars, ),
    path("FetchAllModels/", views.CarsStoreApiMethods.getAllModels, ),
    path("FetchAllBrands/", views.CarsStoreApiMethods.getAllBrands, ),
    path("FetchFilteredCars/", views.CarsStoreApiMethods.getFilteredCars, ),
    path("FetchFilteredModels/", views.CarsStoreApiMethods.getFilteredModels, ),
    path("FetchFilteredCarsByBrandId/", views.CarsStoreApiMethods.getFilteredCarByBrandID, ),
    path("FetchFilteredCarsByModelId/", views.CarsStoreApiMethods.getFilteredCarByModelID, ),
    path("register/", views.CarsStoreApiMethods.register, ),
    path("getAllUsers/", views.CarsStoreApiMethods.getAllUsers, ),
    path("login/", views.CarsStoreApiMethods.login, ),
]