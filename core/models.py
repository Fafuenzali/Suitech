from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id categoría")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la categría")

    def __stf__(self):
        return self.nombreCategoria

class Productos(models.Model):
    sku = models.CharField(max_length=6, primary_key=True, verbose_name="Sku")
    tipo = models.CharField(max_length=15, verbose_name="Tipo")
    marca = models.CharField(max_length=7, verbose_name="Marca Productos")

    def __str_(self):
        return self.sku