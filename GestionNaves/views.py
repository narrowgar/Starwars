from django.shortcuts import render
from .models import Nave,Modelo,Piloto,DueñoNave
from django.views import generic 
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
# Create your views here.

def app(request):
    # utilisamos el comando .all().count() para poder contar todos las naves que tenemos
    num_nave = Nave.objects.all().count()
    num_pilotos = Piloto.objects.all().count()
    num_modelo = Modelo.objects.all().count()
    num_dueñoN = DueñoNave.objects.all().count()

    return render(
        #retornamos un render para renderisar 3 pedidos que son el del request el de la pagina que queremos llamar y el contexto del que queremos agregar.
        request,
        'app.html',
        context={'num_nave':num_nave,'num_pilotos':num_pilotos,'num_modelo':num_modelo,'num_dueñoN':num_dueñoN },
    )
def index(request):
    return render(
        #renderisamos el pedido que es llamar a la  pagina index.html
        request,
        "index.html"
    )
def pag2(request):
    return render(
        request,
        "pag2.html"
    )
def Minijuego2(request):
    return render(
        request,
        "Minijuego2.html"
    )
def enContru(request):
    return render(
        request,
        "enContru.html"
    )
def NaveLista(request):
    #llamamos a todos las naves que estan en la base de datosla base de datos Nave.objects.all()
    nave = Nave.objects.all()
    #en el constexto ingresamos la manera de como llamar todos los datos para la lista
    contexto = {'Naves':nave}
    return render(
        request,
        'Nave.html',
        contexto
    )
def PilotoLista(request):
    #llamamos a todos los pilotos que estan en la base de datosla base de datos Nave.objects.all()
    pilote = Piloto.objects.all()
    contexto = {'Pilotos':pilote}
    return render(
        request,
        'piloto.html',
        contexto
    )
def ModeloLista(request):
    modele = Modelo.objects.all()
    contexto = {'Modelos':modele}
    return render(
        request,
        'Modelo.html',
        contexto
    )
def DueñoLista(request):
    dueñe = DueñoNave.objects.all()
    contexto = {'Dueño':dueñe}
    return render(
        request,
        'duennos.html',
        contexto
    )

      