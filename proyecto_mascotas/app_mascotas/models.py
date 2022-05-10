from django.db import models

# Create your models here.

class Mascota(models.Model):
    
    tipos = (
        ('G', 'Gato'),
        ('P', 'Perro'),
        ('C', 'Conejo'),
        ('H', 'Hamster'),
        )
    
    sexos = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        )
        
    nombre = models.CharField(max_length = 60)
    tipo = models.CharField(max_length = 3, choices = tipos, default = 'X')
    sexo = models.CharField(max_length = 2, choices = sexos, default = 'X')
    fecha_de_nacimiento = models.DateField()
    dueño = models.CharField(max_length = 60)
    observaciones = models.CharField(max_length = 120, blank = True)

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.get_tipo_display())
