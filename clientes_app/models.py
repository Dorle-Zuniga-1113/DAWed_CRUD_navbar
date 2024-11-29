from django.db import models

# Create your models here.
class Clientes(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    numero=models.CharField(max_length=100)
    ciudad= models.CharField(max_length=10)
    numCuenta=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    