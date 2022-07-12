from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_shortner,name="url_shortner"),
    path('<slug:key>/',views.routToURL)
]
