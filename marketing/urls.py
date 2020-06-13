from django.urls import path
from django.contrib import admin
from django.urls import include
from . import views

urlpatterns = [
    #path('', views.index, name='index'),

    # Marketing pages
    path('', views.HomePage.as_view(), name="HomePage"),

    # Subscriber related URLs
    path(r'^signup/$', 'subscribers.views.subscriber_new', name='sub_new'),

    # Admin URL


    # Login/Logout URLs


    # Account related URLs


    # Contact related URLS


    # Communication related URLs
    
]

#Add Django site authentication urls (for login, logout, password management)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]