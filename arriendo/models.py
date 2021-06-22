from django.db import models
from django.conf import settings
from django.db.models.fields import IntegerField

# Create your models here.
class Depto(models.Model):
    
    DEPTO_CATEGORIES = (
        ('VIN','Vina del Mar'),
        ('SER','La Serena'),
        ('PUC','Pucon'),
        ('VIL','Villarrica'),
        ('VAL','Valdivia'),
        ('IQU','Iquique'),
        ('FRU','Frutillar'),
    )
    category = models.CharField(max_length=3, choices=DEPTO_CATEGORIES,default='Iquique')
    precio = models.IntegerField()
    capacidad = models.IntegerField()
    camas = models.IntegerField()

    def __str__(self):
        return self.category

class Reserva(models.Model):
    #id del cliente 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    depto = models.ForeignKey(Depto, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} ha reservado depto en {self.depto}, desde {self.check_in} hasta {self.check_out}' 
