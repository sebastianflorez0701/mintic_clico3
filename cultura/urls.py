from django.urls import path
from  . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("actividades", views.actividad, name="actividad"),
    path("ciudad", views.ciudad, name="ciudad"),
   # path("actividades/",views.activities),
   # path("ciudad/",views.city),
]

