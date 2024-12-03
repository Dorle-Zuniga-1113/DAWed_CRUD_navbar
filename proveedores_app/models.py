from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    productos=models.CharField(max_length=100)
    ciudad= models.CharField(max_length=10)
    distribucion=models.CharField(max_length=100)
    p_mayoreo=models.CharField(max_length=100)
    certificado=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    