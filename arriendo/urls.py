from django.urls import path
from .views import CancelReservaView, DeptoListView, DeptoDetailView, ReservaListView, ubicaciones

app_name='arriendo'

urlpatterns = [
    path('depto_list/', DeptoListView,name='DeptoListView'),
    path('reserva_list/', ReservaListView.as_view(),name='ReservaListView'),#"as_view" pq en views.py esta declaraddo como clase y no como funcion
    path('depto/<category>',DeptoDetailView.as_view(), name='DeptoDetailView'),
    path('ubicaciones/', ubicaciones,name='Ubicaciones'),
    # <pk> es lo qe usan los generic views
    path('reserva/cancel/<pk>',CancelReservaView.as_view(), name='CancelReservaView'),
]