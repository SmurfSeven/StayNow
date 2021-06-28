from arriendo.models import Reserva, Depto

def book_depto(request,depto,check_in,check_out): #request es para obtener el user, depto la ciudad
    # creación de un objeto reserva y se guarda
    reserva = Reserva.objects.create(
        user = request.user,
        depto = depto,
        check_in = check_in,
        check_out = check_out,
    )
    reserva.save()

    return reserva