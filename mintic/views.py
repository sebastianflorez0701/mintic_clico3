from django.shortcuts import render

def home(request):
  return render(request,"index.html", None)

def activities(request):
  return render(request,"actividades.html", None)

def city(request):
  return render(request,"ciudad.html", None)