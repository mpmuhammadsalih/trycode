
from django.contrib import admin
from django.urls import path
from .views import Myview

urlpatterns = [
    path('home/',Myview.as_view()),
    path('aboutus/',Myview.as_view()),
    
]
