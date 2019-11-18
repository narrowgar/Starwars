from django.contrib import admin
from .models import Nave,Modelo,Piloto,DueñoNave
# Registramos los modelos creados para poder administrar los modelos creados anteriormente.
admin.site.register(Nave)
admin.site.register(Modelo)
admin.site.register(Piloto)
admin.site.register(DueñoNave)