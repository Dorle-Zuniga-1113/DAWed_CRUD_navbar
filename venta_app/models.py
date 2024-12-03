from django.db import models

# Create your models here.
class Ventas(models.Model):
    id_venta=models.CharField(primary_key=True,max_length=6)
    id_cliente=models.CharField(max_length=100)
    id_empleado=models.CharField(max_length=100)
    id_producto = models.CharField(max_length=10)
    factura=models.CharField(max_length=100)
    descuento= models.CharField(max_length=10)
    fecha_venta = models.DateField(null=True, blank=True)
    pago=models.CharField(max_length=100)
    iva=models.CharField(max_length=100)
    
    def __str__(self):
        return self.factura
    