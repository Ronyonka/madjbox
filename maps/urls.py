from django.urls import path, include
from .views import *

urlpatterns = [
    path('', default_map, name="default"),
]
