#from django.db import reset_queries
from arriendo.models import Depto

def get_depto_category_human_format(category):
    '''
    Funcion que toma la key de una ciudad desde depto_category y la retorna formato lenguaje humano
    (ejemplo "IQU" >> retorna "Iquique")
    '''
    
    # se importan los objetos de la bd para obtener los nombres de categorias(ciudades)
    depto = Depto.objects.all()[0]
    depto_category = dict(depto.DEPTO_CATEGORIES).get(category, None) # ".get(depto.category" obtiene la key de la tupla
    
    #retorna la key de ese depto en posicion[0]
    return depto_category

# https://www.tutorialspoint.com/python/dictionary_get.htm

'''
def get_depto_from_category():
    # se busca/filtra por depto qe coincida con el criterio de busqueda de  var "category" y se hace una lista de
    # esos deptos en la var "depto_list"
    depto_list = Depto.objects.filter(category=category)
        
    # si con el filtro aplicado se resuelve qe hay deptos con esa categoria(ciudad)...
    if len(depto_list)>0: 
        depto = depto_list[0] # el primer depto libre qe encuentre segun categoria(en este caso ciudad)
        depto_category = dict(depto.DEPTO_CATEGORIES).get(depto.category, None) # ".get(depto.category" obtiene la key de la tupla
        
        #retorna la key de ese depto en posicion[0]
        return depto_category
    else:
        # si no encuentra nada con el filtro retorna nada
        None  
'''