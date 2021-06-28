from arriendo.models import Depto
from django.urls import reverse


def get_depto_cat_url_list():
    '''
    Funcion qe retorna Lista de: Ciudad depto y ciudad url
    '''

    # se obtiene el primer item qe coincida con el criterio de busqueda
    # (en el caso de haber mas de 1 depto x categoria/ciudad, solo es necesario nombrar 1 vez la ciudad)
    depto = Depto.objects.all()[0] 
    
    # diccionario para la tupla "depto_categories" con las ciudades existentes
    depto_categories = dict(depto.DEPTO_CATEGORIES)

    # inicializacion list vacia
    depto_cat_url_list = []

    # for loop para rellenar depto_cat_url_list
    for category in depto_categories: 

        # se obtiene el nombre de la ciudad y se guarda en var "depto_category"
        depto_category = depto_categories.get(category) # funcion ".get" obtiene el value (y no key) de una tupla ojo ahi

        # IMPORTANTE AQUI, se pasa la "key" de la tupla (category) y no el "value" (depto_category), sino no funcionaria el url
        depto_url = reverse('arriendo:DeptoDetailView',kwargs={'category':category})
        
        depto_cat_url_list.append((depto_category,depto_url))#tupla que contiene el depto y la url del depto
    
    return depto_cat_url_list