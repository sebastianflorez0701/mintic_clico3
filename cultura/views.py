from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"cultura/index.html")

def actividad(request):
    return render(request,"cultura/actividades.html")

def ciudad(request):
    return render(request,"cultura/ciudad.html")
