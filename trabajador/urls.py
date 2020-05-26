from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_trabajador, name='lista_trabajador'),
    path('<int:id>', views.ver_trabajador, name='ver_trabajador'),
    path('agregar', views.agregar_trabajador, name='agregar_trabajador'),
    path('eliminar/<int:pk>', views.eliminar_trabajador,
         name='eliminar_trabajador'),
    path('modificar/<int:id>', views.modificar_trabajador,
         name='modificar_trabajador'),
]
