from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.coll, name = "coll"),
    path('', views.find, name="find"),
]