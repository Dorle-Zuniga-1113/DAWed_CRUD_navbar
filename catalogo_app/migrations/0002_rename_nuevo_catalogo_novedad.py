# Generated by Django 5.1 on 2024-12-03 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogo',
            old_name='nuevo',
            new_name='novedad',
        ),
    ]