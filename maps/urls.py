from django.urls import path, include
from .views import *

urlpatterns = [
    path('', default_map, name="default"),
    path('home', home_map, name="home"),
    path('another', another_map, name="another"),
    path('pics', picture_gallery, name="pics"),
]
