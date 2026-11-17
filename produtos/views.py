from django.shortcuts import render, redirect
from .forms import ProdutoForm


def cadastrar_produto(request):
    if request.method == 'POST':
        formulario = ProdutoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')

    else:
        formulario = ProdutoForm()

    return render(request, 'produtos/cadastrar.html', {
        'formulario': formulario
    })
