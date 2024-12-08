# Generated by Django 5.1.2 on 2024-11-29 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('id_cliente', models.CharField(max_length=100)),
                ('id_empleado', models.CharField(max_length=100)),
                ('id_producto', models.CharField(max_length=10)),
                ('factura', models.CharField(max_length=100)),
                ('descuento', models.CharField(max_length=10)),
                ('fecha_venta', models.DateField(blank=True, null=True)),
                ('pago', models.CharField(max_length=100)),
                ('iva', models.CharField(max_length=100)),
            ],
        ),
    ]
