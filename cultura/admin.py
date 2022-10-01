from django.contrib import admin
from .models import Ciudades,Actividades

# Registro de Modelos al administrador de datos de la aplicacion cultura
admin.site.register(Ciudades)
admin.site.register(Actividades)

