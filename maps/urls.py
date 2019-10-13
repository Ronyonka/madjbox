from django.urls import path, include
from .views import *

urlpatterns = [
    path('', default_map, name="default"),
    path('home', home_map, name="home"),
]
