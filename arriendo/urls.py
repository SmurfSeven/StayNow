from django.urls import path
from .views import DeptoListView, ReservaView, ReservaView, DeptoDetailView

app_name='arriendo'

urlpatterns = [
    path('depto_list/', DeptoListView,name='DeptoList'),
    path('reserva_list/', ReservaView,name='ReservaList'),#"as_view" pq en views.py esta declaraddo como clase y no como funcion
    path('reserva/',ReservaView.as_view(), name='ReservaView'),
    path('depto/<category>',DeptoDetailView.as_view(), name='DeptoDetailView'),
]