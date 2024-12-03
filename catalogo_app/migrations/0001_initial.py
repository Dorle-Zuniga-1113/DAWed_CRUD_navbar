# Generated by Django 5.1.2 on 2024-11-29 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('promocion', models.CharField(max_length=100)),
                ('coleccion', models.CharField(max_length=100)),
                ('nuevo', models.CharField(max_length=100)),
            ],
        ),
    ]