# Generated by Django 3.2.4 on 2021-07-12 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactos',
            fields=[
                ('ID', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25, verbose_name='Nombre')),
                ('Apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('Correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('Telefono', models.CharField(max_length=12, verbose_name='Telefono')),
                ('Mensaje', models.CharField(max_length=120, verbose_name='Mensaje')),
                ('FechaEnvio', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]
