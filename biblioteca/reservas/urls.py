# URLs (reservas/urls.py)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),  # Rota para listar livros
    path('reservar/<int:livro_id>/', views.reservar_livro, name='reservar_livro'),  # Rota para reservar um livro
    path('confirmacao/', views.confirmacao_reserva, name='confirmacao_reserva'),  # Rota para confirmar a reserva
]
