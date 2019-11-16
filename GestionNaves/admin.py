from django.contrib import admin
from .models import Nave,Modelo,Piloto,DueñoNave
# Register your models here.
admin.site.register(Nave)
admin.site.register(Modelo)
admin.site.register(Piloto)
admin.site.register(DueñoNave)