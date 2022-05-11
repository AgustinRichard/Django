from email import charset
from django.db import models

# Create your models here.
class Articulo(models.Model):
    CAGEGORIAS_CHOICES = (
    	('hardware', 'Hardware'),
    	('software', 'Software'),
        ('insumos', 'Insumos'),
        ('servicios', 'Servicios'),
        ('varios', 'Varios'),
	)

    codigo = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=10,
	choices=CAGEGORIAS_CHOICES, default='hardware')

    def __str__(self):
        return self.descripcion

