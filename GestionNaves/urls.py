from django.urls import path
from . import views

urlpatterns = [
    #utilisamos path('',views.index,name='index') para iniciar al principio la view llamada index
    path('',views.index,name='index'),
    #en el path escribimos donde esta primero la pagina templates/pag2.html para que el views tome este.
    path('templates/pag2.html',views.pag2,name='pag2'),
    path('templates/Minijuego2.html',views.Minijuego2,name='Minijuego2'),
    path('templates/enContru.html',views.enContru,name='enContru'),
    path('templates/app.html',views.app,name='app'),
    path('templates/Nave.html', views.NaveLista, name='Nave'),
    path('templates/Piloto.html', views.PilotoLista, name='piloto'),
    path('templates/Modelo.html', views.ModeloLista, name='modelo'),
    path('templates/dueños.html', views.DueñoLista, name='duenno'),
    path('admin/', views.admin,name = 'admin'),
    path('templates/post.html',views.contacto, name= 'post')
]
