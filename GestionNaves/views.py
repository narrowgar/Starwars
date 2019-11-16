from django.shortcuts import render
from .models import Nave,Modelo,Piloto,DueñoNave
from django.views import generic 
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
# Create your views here.

def app(request):
    num_nave = Nave.objects.all().count()
    num_pilotos = Piloto.objects.all().count()
    num_modelo = Modelo.objects.all().count()
    num_dueñoN = DueñoNave.objects.all().count()

    return render(
        request,
        'app.html',
        context={'num_nave':num_nave,'num_pilotos':num_pilotos,'num_modelo':num_modelo,'num_dueñoN':num_dueñoN },
    )
def index(request):
    return render(
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
    nave = Nave.objects.all()
    contexto = {'Naves':nave}
    return render(
        request,
        'Nave.html',
        contexto
    )
def PilotoLista(request):
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

      