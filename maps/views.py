from django.shortcuts import render
from decouple import config


def default_map(request):
    mapbox_access_token = config('ACCESS_TOKEN')
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })