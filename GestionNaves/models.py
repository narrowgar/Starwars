from django.db import models

# Create your models here.
class Modelo(models.Model):
    #se crea el model Modelo el cual tiene 3 CharField()
    nombreModelo = models.CharField(max_length=200)
    tipoModelo = models.CharField(max_length=200)
    idModelo = models.CharField(max_length=200)

    def __str__(self):
        #Utilistando __str__ escribimos el id del Modelo 
        return self.idModelo

class Nave(models.Model):
    nombreNave = models.CharField(max_length=200)
    #utilisamos el comando ForeignKey para obtener la id del Modelo
    Modelo = models.ForeignKey(Modelo,on_delete = models.CASCADE,null = False)
    #utilisamos el comando DateTime para ingresar una fecha
    fechaCreacion = models.DateField()
    idNave = models.CharField(max_length=200)
    #se utiliza el comando ImageField para poder ingresar la imagen en la base de datos
    fotoNave = models.ImageField(upload_to= 'img',default = 'static/img')

    def __str__(self):
        #Utilistando __str__ escribimos el id de la Nave
        return self.idNave
class Piloto(models.Model):
    nombrePiloto = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    #El PositiveIntegerField() es un campo que nos permite solo ingresar datos mayor a 0 y que no sean decimales 
    edad=models.PositiveIntegerField()
    fechnac = models.DateField()
    fotoPiloto = models.ImageField(upload_to= 'img',default = 'img')

    def __str__(self):
        return "{0}  ({1})".format(self.nombrePiloto, self.apellidos)
class DueñoNave(models.Model):
    Piloto = models.ForeignKey(Piloto,null =False,blank = False, on_delete = models.CASCADE)
    Nave = models.ForeignKey(Nave,null =False,blank = False, on_delete = models.CASCADE)
    #utilisamos el DateTimeField para que ingrese la fecha y la hora en que se adquirio la nave por el piloto
    fechAdquisicion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #utilisamos la cadena para que el __str__ escriba de una manera especifica el texto
        cadena = "{0} => {1}"
        return cadena.format(self.Piloto, self.Nave)

     
