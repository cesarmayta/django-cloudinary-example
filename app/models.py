from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = CloudinaryField('imagen')