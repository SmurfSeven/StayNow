from arriendo.models import Depto
from .availability import check_availability

def get_available_deptos(category, check_in, check_out):
    '''
    Funcion qe toma una categoria(ciudad) y retorna una lista de deptos
    '''
    
    #lista de deptos qe satisfacen el filtro de categoria(ciudad)
    depto_list = Depto.objects.filter(category=category)

  # init empty list
    available_deptos=[]

    # populate the list
    for depto in depto_list:
        #se obtiene check_in + check_out desde el form.cleaned_data ingresado por el usuario en la web
        if check_availability(depto, check_in, check_out): 
            available_deptos.append(depto) # .append agrega un elemento a una lista
    
    # revisa el largo de la lista, si es mayor a 0 retornara la lista de deptos, sino retorna nara
    if len(available_deptos) > 0:
        return available_deptos
    else:
        return None