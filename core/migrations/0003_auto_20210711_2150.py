# Generated by Django 3.2.4 on 2021-07-12 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contactos',
            new_name='Contacto',
        ),
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]
