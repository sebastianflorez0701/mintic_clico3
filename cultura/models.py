from email.policy import default
from django.db import models

class Ciudades(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
class Actividades(models.Model):
    precio = models.IntegerField(default=0)
    valoracion = models.PositiveSmallIntegerField(blank=True)
    ciudad = models.ForeignKey(Ciudades,on_delete=models.CASCADE)
    comentario = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.precio
    
    def valor(self):
        return self.valoracion
    
    
