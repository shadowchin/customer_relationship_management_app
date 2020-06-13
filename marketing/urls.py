from django.urls import path
from django.contrib import admin
from django.urls import include
from . import views

urlpatterns = [
    # Marketing pages
    path('', views.HomePage.as_view(), name="marketing/HomePage"),
]