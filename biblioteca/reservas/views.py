#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Reserva

def lista_livros(request):
    livros = Livro.objects.filter(disponivel=True)
    return render(request, 'reservas/lista_livros.html', {'livros': livros})

def reservar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id, disponivel=True)
    if request.method == 'POST':
        usuario = request.POST['usuario']
        reserva = Reserva(livro=livro, usuario=usuario)
        reserva.save()
        livro.disponivel = False
        livro.save()
        return redirect('confirmacao_reserva')
    return render(request, 'reservas/reservar_livro.html', {'livro': livro})

def confirmacao_reserva(request):
    return render(request, 'reservas/confirmacao_reserva.html')
