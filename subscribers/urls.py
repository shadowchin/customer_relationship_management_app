from django.urls import path
from django.contrib import admin
from django.urls import include
from . import views

urlpatterns = [
    # Subscriber pages
    #path('subscriber_new', views.subscriber_new, name="subscriber/subcriber_new"),
    
    # ex: /subscribers/
    path('', views.subscriber_new, name='subscriber_new'),
]