# Generated by Django 5.1 on 2024-12-03 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_app', '0002_rename_nuevo_catalogo_novedad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogo',
            old_name='novedad',
            new_name='novedades',
        ),
    ]