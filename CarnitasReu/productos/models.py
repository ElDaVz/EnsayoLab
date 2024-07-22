from django.db import models

class Producto(models.Model):
    TIPO_CHOICES = [
        ('Carne', 'Carne'),
        ('Bebida', 'Bebida'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.nombre

