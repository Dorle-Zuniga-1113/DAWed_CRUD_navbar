# Generated by Django 5.1.2 on 2024-11-27 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='caducidad',
            field=models.DateField(blank=True, null=True),
        ),
    ]