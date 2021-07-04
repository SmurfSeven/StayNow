from django import http
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Depto, Reserva
from .forms import AvailabilityForm, CustomCreationForm
from arriendo.reserva_functions.availability import check_availability
from arriendo.reserva_functions.get_depto_cat_url_list import get_depto_cat_url_list
from arriendo.reserva_functions.get_depto_category_human_format import get_depto_category_human_format
from arriendo.reserva_functions.get_available_deptos import get_available_deptos
from arriendo.reserva_functions.book_depto import book_depto
from django.contrib.auth import authenticate,login
from django.contrib import messages



# Create your views here.
def DeptoListView(request):
    depto_category_url_list = get_depto_cat_url_list()

    context = {
        "depto_list": depto_category_url_list,
    }
    
    return render (request,'depto_list_view.html', context)

# retorna la lista de reservas para cada usuario (y para admin muestra TODAS)
class ReservaListView(ListView):
    model = Reserva

    #aqui se hace la referencia la template, en una variable,
    #  y no en un "return render" como es el caso de una "def"
    template_name = 'reserva_list_view.html'
    
    def get_queryset(self,*args, **kwargs):
        # usuario admin podra ver TODAS las reservas
        if self.request.user.is_staff:
            reserva_list = Reserva.objects.all()
            return reserva_list

        # usuario normal solo podra ver SUS PROPIAS reservas
        else:
            reserva_list = Reserva.objects.filter(user=self.request.user)
            return reserva_list
    

class DeptoDetailView(View):
    
    # generic view based DeptoDetailView
    def get(self, request, *args, **kwargs):

        #se obtiene keyword argument desde la misma url del browser (ejemplo: desde depto iquique obtiene "IQU")
        category = self.kwargs.get('category',None)#segundo parametro = none, por si algun usuario escribe algo en la url estropearia la captura de la categoria
        
        # se obtiene categoria(ciudad) en human readable ("La Serena" en vez de 'SER')
        human_format_depto_category = get_depto_category_human_format(category)
       
        # se inicializa form vacio
        form = AvailabilityForm()

        if human_format_depto_category is not None:
            context={
            'depto_category': human_format_depto_category,
            'form': form #referencia a availability form
            }
            return render(request,'depto_detail_view.html',context)
        else:
            return HttpResponse('Departamento No Existe!')
        
  
    def post(self, request, *args, **kwargs):
        # se obtiene Depto categoria-ciudad desde kwargs
        category = self.kwargs.get('category',None)
        
        # pass request.POST into AvailibilityForm
        form= AvailabilityForm(request.POST)

        # revisa validez del form
        if form.is_valid():
            data = form.cleaned_data # form. cleaned_data is where all validated fields are stored.

        # se obtiene departamentos disponibles segun categoria y check_in + check_out ingresado x un cliente
        available_deptos = get_available_deptos(category,data['check_in'],data['check_out'])

        # checkea si hay deptos disponibles (si hay deptos disponibles en la ciudad escogida para arrendar...)
        if available_deptos is not None:
            # reserva el depto (el primero "[0]" de la categoria qe halle disponible)
            reserva = book_depto(request,available_deptos[0],
                       data['check_in'],data['check_out'])
            #messages.success(request,"Reserva exitosa!")
            return HttpResponse(reserva)
        else:
            #messages.error(request,"error lo sentimos")
            return HttpResponse('lo sentimos, este departamento se encuentra ocupado para tales fechas. Por favor intente con otra fecha')

       

class CancelReservaView(DeleteView):
    model = Reserva

    template_name = 'reserva_cancel_view.html'

    #al eliminar exitosamente una reserva, redirigirse lista de resrvas
    success_url = reverse_lazy('arriendo:ReservaListView')

def ubicaciones(request):
  
    ciudades = [
        ['map_vina','Viña del Mar'],
        ['map_serena','La Serena'],
        ['map_pucon','Pucon'],
        ['map_iquique','Iquique'],
        ['map_villarica','Villarica'],
        ['map_valdivia','Valdivia'],
        ['map_frutillar','Frutillar']
    ]

    data = {
        'ciudades' : ciudades
    }
    
    return render (request,'ubicaciones.html', data)
    
def registro(request):
    data = {
        'form': CustomCreationForm
    }

    if request.method=='POST':
        formulario = CustomCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            #para qe el usuario recien creado quede logueado altiro
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            #messages.success(request, "te has registrado exitosamente")
            #redirigir al home
            return redirect(to="arriendo:DeptoListView")

    return render(request,'registration/registro.html',data)       

# CLASE COMENTADA A CONTINUACION PQ SE INTEGRO ESTA FUNCIONALIDAD
# EN la clase DeptoDetailView 

# class ReservaView(FormView):
#     form_class = AvailabilityForm
#     template_name = 'availability_form.html'

#     def form_valid(self, form):
#         data = form.cleaned_data
#         depto_list = Depto.objects.filter(category=data['depto_category'])
#         available_deptos=[]

#         for depto in depto_list:
#             if check_availability(depto,data['check_in'],data['check_out']):
#                 available_deptos.append(depto)
        

#         if len(available_deptos) > 0:
#             depto = available_deptos[0]
#             reserva = Reserva.objects.create(
#             user = self.request.user,
#             depto = depto,
#             check_in = data['check_in'],
#             check_out = data['check_out']
#             )
#             reserva.save()
#             return HttpResponse(reserva)
#         else:
#             return HttpResponse('lo sentimos, este departamento se encuentra ocupado para tales fechas. Por favor intente con otra fecha')


        