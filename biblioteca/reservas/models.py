from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)  # Nome do usuário
    data_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} - {self.livro.titulo}'
