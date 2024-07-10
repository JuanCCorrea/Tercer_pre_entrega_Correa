
from django.urls import path, include
from .views import *

urlpatterns = [
    path ('', home, name = "home"),
    path ('clases/', clases, name = "clases"),
    path ('horario/', horario, name = "horario"),
    path ('reserva/', reserva, name = "reserva"),
    path ('acerca/', acerca, name = "acerca"),
    path ('clasesForm/', claseForm, name = "clasesForm"),
    path ('horarioForm/', HorarioForm, name = "horarioForm"),
    path ('reservaForm/', reservaForm, name = "reservaForm"),
    path ('buscarClases/', buscarClases, name = "buscarClases"),
    path ('encontrarClases/', encontrarClases, name = "encontrarClases"),
    
    
]
