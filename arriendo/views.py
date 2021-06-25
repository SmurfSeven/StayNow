from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Depto, Reserva
from .forms import AvailabilityForm
from arriendo.reserva_functions.availability import check_availability

# Create your views here.
def DeptoListView(request):
    depto = Depto.objects.all()[0]
    depto_categories = dict(depto.DEPTO_CATEGORIES)
    
    depto_values = depto_categories.values()
    depto_list = []

    for depto_category in depto_categories:
        depto = depto_categories.get(depto_category)
        depto_url = reverse('arriendo:DeptoDetailView',kwargs={'category':depto_category})
        
        depto_list.append((depto,depto_url))

    context = {
        "depto_list": depto_list,
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
    def get(self, request, *args, **kwargs):
        #se obtiene categoria desde la misma url del browser
        category = self.kwargs.get('category',None)#segundo parametro = none, por si algun usuario escribe algo en la url estropearia la captura de la categoria
        form = AvailabilityForm()
        depto_list = Depto.objects.filter(category=category)
        
        if len(depto_list)>0: 
            depto = depto_list[0] # el primer depto libre qe encuentre segun categoria(en este caso ciudad)
            depto_category = dict(depto.DEPTO_CATEGORIES).get(depto.category, None)
            context={
            'depto_category': depto_category,
            'form': form
            }
            return render(request,'depto_detail_view.html',context) 
        else:
            return HttpResponse('Departamento No Existe!')


    
    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category',None)
        depto_list = Depto.objects.filter(category=category)
        form= AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
        
        available_deptos=[]

        for depto in depto_list:
            if check_availability(depto,data['check_in'],data['check_out']):
                available_deptos.append(depto)
        

        if len(available_deptos) > 0:
            depto = available_deptos[0]
            reserva = Reserva.objects.create(
            user = self.request.user,
            depto = depto,
            check_in = data['check_in'],
            check_out = data['check_out']
            )
            reserva.save()
            return HttpResponse(reserva)
        else:
            return HttpResponse('lo sentimos, este departamento se encuentra ocupado para tales fechas. Por favor intente con otra fecha')

class CancelReservaView(DeleteView):
    model = Reserva

    template_name = 'reserva_cancel_view.html'

    #al eliminar exitosamente una reserva, redirigirse lista de resrvas
    success_url = reverse_lazy('arriendo:ReservaListView')

        

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


        