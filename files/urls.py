from django.urls import path, include
from .views import *

urlpatterns = [
    path("", upload_file, name="upload"),
    path("here", test_view, name="test_view"),
]
