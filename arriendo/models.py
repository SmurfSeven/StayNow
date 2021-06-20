from django.db import models

# Create your models here.
class Depto(models.Model):
    precio = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    camas = models.IntegerField()
    
    def __str__(self):
        return self.ciudad
