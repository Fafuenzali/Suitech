from django.db import models
import datetime
# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id categoría")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la categría")

    def __stf__(self):
        return self.nombreCategoria

class Producto(models.Model):
    sku = models.CharField(max_length=6, primary_key=True, verbose_name="Sku")
    tipo = models.CharField(max_length=15, verbose_name="Tipo")
    marca = models.CharField(max_length=7, verbose_name="Marca Productos")

    def __str__(self):
        return self.sku

class Contacto(models.Model):
    ID = models.CharField(max_length=8, primary_key=True, verbose_name="ID")
    Nombre = models.CharField(max_length=25,verbose_name="Nombre")
    Apellidos = models.CharField(max_length=50, verbose_name="Apellidos")
    Correo = models.CharField(max_length=50, verbose_name="Correo")
    Telefono = models.CharField(max_length=12, verbose_name="Telefono")
    Mensaje =models.CharField(max_length=120, verbose_name="Mensaje")
    FechaEnvio =models.DateField(("Date"), default=datetime.date.today)
    
    def __str__(self):
        return self.ID