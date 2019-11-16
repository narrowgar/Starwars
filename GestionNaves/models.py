from django.db import models

# Create your models here.
class Modelo(models.Model):
    nombreModelo = models.CharField(max_length=200)
    tipoModelo = models.CharField(max_length=200)
    idModelo = models.CharField(max_length=200)

    def __str__(self):
        return self.idModelo

class Nave(models.Model):
    nombreNave = models.CharField(max_length=200)
    Modelo = models.ForeignKey(Modelo,on_delete = models.CASCADE,null = False)
    fechaCreacion = models.DateField()
    idNave = models.CharField(max_length=200)

    def __str__(self):
        return self.idNave
class Piloto(models.Model):
    nombrePiloto = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    edad=models.PositiveIntegerField()
    fechnac = models.DateField()

    def __str__(self):
        return "{0}  ({1})".format(self.nombrePiloto, self.apellidos)
class DueñoNave(models.Model):
    Piloto = models.ForeignKey(Piloto,null =False,blank = False, on_delete = models.CASCADE)
    Nave = models.ForeignKey(Nave,null =False,blank = False, on_delete = models.CASCADE)
    fechAdquisicion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Piloto, self.Nave)

     
