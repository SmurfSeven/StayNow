from django.db import models
from django.conf import settings
from django.db.models.fields import IntegerField

#para redireccion a eliminar una reserva 
from django.urls import reverse_lazy

# Create your models here.
class Depto(models.Model):
    
    DEPTO_CATEGORIES = (
        #1er parametro = key value
        #2do parametro = value neto
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
    
    # fx que posteriormente servirá para qe un usuario pueda ver su lista de reservas con el nombre de categoria(ciudad)
    # completo en vez del acronimo. (osea 'Pucon' en vez de 'PUC')
    def get_depto_category(self):
        depto_categories = dict(self.depto.DEPTO_CATEGORIES)
        depto_category = depto_categories.get(self.depto.category)
        return depto_category
    
    def get_cancel_reserva_url(self):
        return reverse_lazy('arriendo:CancelReservaView',args=[self.pk,])


