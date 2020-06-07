from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),

    # Marketing pages
    path('', views.HomePage.as_view(), name="marketing/home"),

    # Subscriber related URLs


    # Admin URL


    # Login/Logout URLs


    # Account related URLs


    # Contact related URLS


    # Communication related URLs
    
]