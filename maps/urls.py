from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_map, name="home"),
    path('default', default_map, name="default"),
    path('another', another_map, name="another"),
    path('pics', picture_gallery, name="pics"),
]
