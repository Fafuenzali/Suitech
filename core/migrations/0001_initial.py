# Generated by Django 3.2.4 on 2021-06-28 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id categoría')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categría')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('sku', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Sku')),
                ('tipo', models.CharField(max_length=15, verbose_name='Tipo')),
                ('marca', models.CharField(max_length=7, verbose_name='Marca Productos')),
            ],
        ),
    ]
