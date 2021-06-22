import datetime
from arriendo.models import Depto, Reserva

def check_availability(depto, check_in,check_out):
    avail_list = []
    reserva_list = Reserva.objects.filter(depto=depto)
    for reservas in reserva_list:
        if reservas.check_in > check_out or reservas.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list) # "all" or "any", all retorna true si TODOS son true
     
