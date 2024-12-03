from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    numero=models.CharField(max_length=100)
    ciudad= models.CharField(max_length=10)
    numCuenta=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    email=models.CharField(max_length=100 , null=True)
    def __str__(self):
        return self.nombre
    