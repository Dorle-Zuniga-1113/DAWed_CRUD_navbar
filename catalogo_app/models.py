from django.db import models

# Create your models here.
class Catalogo(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    nombre = models.CharField(max_length=100)
    promocion= models.CharField(max_length=100)
    coleccion=models.CharField(max_length=100)
    novedades=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
        