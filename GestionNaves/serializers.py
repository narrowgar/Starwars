from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Nave,Modelo,Piloto,DueñoNave

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups',]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class NaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Nave
        fields = ['nombreNave','Modelo','fechaCreacion','idNave','fotoNave']

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Modelo
        fields = ['nombreModelo','tipoModelo','idModelo']

class PilotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Piloto
        fields = ['nombrePiloto','apellidos','edad','fechnac','fotoPiloto']
