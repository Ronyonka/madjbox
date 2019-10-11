from django.shortcuts import render
from decouple import config
from madjbox.settings.base import ACCESS_TOKEN


def default_map(request):
    mapbox_access_token = ACCESS_TOKEN
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })