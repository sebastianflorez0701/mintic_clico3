from email.policy import default
from django.db import models

class Ciudades(models.Model):
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre
    
class Actividades(models.Model):
    nombre_actividad = models.CharField(max_length=40)
    precio = models.IntegerField(default=0)
    valoracion = models.PositiveSmallIntegerField(blank=True)
    ciudad = models.ForeignKey(Ciudades,on_delete=models.CASCADE)
    comentario = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='media/')
    
    def valor(self):
        return self.valoracion
    
    
