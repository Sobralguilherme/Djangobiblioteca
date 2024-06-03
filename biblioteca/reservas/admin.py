from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Livro, Reserva

admin.site.register(Livro)
admin.site.register(Reserva)
