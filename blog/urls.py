# -*- coding: utf-8 -*-

#from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('demandes/', views.demandes, name='blog-demandes'),
    path('demandeurs/', views.demandeurs, name='blog-demandeurs'),
    #path('blog/', BlogConfig(AppConfig):.site.urls),
]