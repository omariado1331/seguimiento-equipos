from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Bienvenido al sistema de seguimiento de equipos para el empadronamiento masivo.")