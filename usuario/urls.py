from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuario, name='lista_usuario'),
    path('<int:id>', views.ver_usuario, name='ver_usuario'),
    path('agregar', views.agregar_usuario, name='agregar_usuario'),
    path('eliminar/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),
    path('modificar/<int:id>', views.modificar_usuario, name='modificar_usuario'),
    path('cambiar/<int:id>', views.cambiar_contrasena, name='cambiar_contrasena'),
]
