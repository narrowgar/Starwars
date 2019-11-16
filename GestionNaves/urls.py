from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('templates/pag2.html',views.pag2,name='pag2'),
    path('templates/Minijuego2.html',views.Minijuego2,name='Minijuego2'),
    path('templates/enContru.html',views.enContru,name='enContru'),
    path('templates/app.html',views.app,name='app'),
    path('templates/Nave.html', views.NaveLista, name='Nave'),
    path('templates/Piloto.html', views.PilotoLista, name='piloto'),
    path('templates/Modelo.html', views.ModeloLista, name='modelo'),
     path('templates/dueños.html', views.DueñoLista, name='duenno')
]
