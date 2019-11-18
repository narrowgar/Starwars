from django.shortcuts import render
from .models import Nave,Modelo,Piloto,DueñoNave
from django.views import generic 
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.template import loader, Context
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from .Form import Formulario
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
def admin(request):
    return render(
        request,
        "http://127.0.0.1:8000/admin"
    )
def contacto(request):
    if request.method == 'POST': #Si el formulario es enviado#
        form = Formulario(request.POST)
        if form.is_valid():#Si es valido se procesan los datos
            return HttpResponseRedirect ('Starwars/GestionNaves/') #y se redirige a la url
    else:
        form = Formulario() #formulario vacio
    return render(request, 'post.html',{'form': form,})   