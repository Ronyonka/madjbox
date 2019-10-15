from django.shortcuts import render
from decouple import config
from madjbox.settings.base import ACCESS_TOKEN
from wstf import LongLat, projo1


def default_map(request):
    mapbox_access_token = 'pk.eyJ1Ijoicm9ueW9ua2EiLCJhIjoiY2sxbTF1cjlrMDdkdTNpcDZyNmQ3eG9xeCJ9.GwSPf8q-E9jtvrRrVPgksg'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })

def home_map(request):
    longlat = LongLat()
    projo = projo1()
    return render(request, 'home.html', {'longlat':longlat, 'projo':projo})