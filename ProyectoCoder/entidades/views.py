from django.shortcuts import render
from .models import *
from .forms import *

def home(request):
    return render(request, 'entidades/index.html')

def clases(request):
    contexto = {"clases": Clases.objects.all()}
    return render(request, 'entidades/clases.html', contexto)

def horario(request):
    contexto = {"horario": Horario.objects.all()}
    return render(request, 'entidades/horario.html', contexto)

def reserva(request):
    contexto = {"reserva": Reserva.objects.all()}
    return render(request, 'entidades/reserva.html', contexto)

def acerca(request):
    return render(request, 'entidades/acerca.html')

def claseForm(request):
    if request.method == "POST":
        miForm = clasesForm(request.POST)
        if miForm.is_valid():
            clase_clases = miForm.cleaned_data.get("clases")
            clase_valor = miForm.cleaned_data.get("valor")
            clase = Clases(clases= clase_clases, valor= clase_valor)
            clase.save()
            contexto = {"clases": Clases.objects.all()}
            return render(request, 'entidades/clases.html', contexto)
    else:
        miForm = clasesForm()  
    return render(request, 'entidades/clasesForm.html',{"form": miForm})



def HorarioForm(request):
    if request.method == "POST":
        miForm = horarioForm(request.POST)
        if miForm.is_valid():
            horario_horario = miForm.cleaned_data.get("horario")
            horario = Horario(horario= horario_horario)
            horario.save()
            contexto = {"horario": Horario.objects.all()}
            return render(request, 'entidades/horario.html', contexto)
    else:
        miForm = horarioForm()   
    return render(request, 'entidades/horarioForm.html',{"form": miForm})


def reservaForm(request):
    if request.method == "POST":
        miForm = ReservaForm(request.POST)
        if miForm.is_valid():
            reserva_nombre = miForm.cleaned_data.get("nombre")
            reserva_apellido = miForm.cleaned_data.get("apellido")
            reserva_email = miForm.cleaned_data.get("email")
            reserva_fecha = miForm.cleaned_data.get("fecha")
            reserva = Reserva(nombre = reserva_nombre, apellido = reserva_apellido, email = reserva_email, fecha = reserva_fecha )
            reserva.save()
            contexto = {"reserva": Reserva.objects.all()}
            return render(request, 'entidades/reserva.html', contexto)
    else:
        miForm = ReservaForm()
    return render(request, 'entidades/reservaForm.html',{"form": miForm})


def buscarClases(request):
    return render(request, 'entidades/buscar.html')


def encontrarClases(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clases = Clases.objects.filter(clases__icontains = patron)
        contexto = {"clases": clases}
    else:
        contexto = {"clases": Clases.objects.all()}
        
    return render(request, 'entidades/clases.html', contexto) 
        
    