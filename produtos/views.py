from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto, Categoria
from django.db.models import Q
from django.core.paginator import Paginator


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



def listar_produtos(request):
    categorias = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')
    busca = request.GET.get('busca', '').strip()

    produtos = Produto.objects.all()

    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)

    if busca:
        produtos = produtos.filter(
            Q(nome__icontains=busca) |
            Q(codigo__icontains=busca)
        )

    ordenacao = request.GET.get('ordenacao', 'nome')

    ordenacoes = {
        'nome': 'nome',
        '-nome': '-nome',
        'preco': 'preco',
        '-preco': '-preco',
        'quantidade': 'quantidade',
        '-quantidade': '-quantidade',
    }

    produtos = produtos.order_by(
        ordenacoes.get(ordenacao, 'nome')
    )

    paginador = Paginator(produtos, 5)
    numero_pagina = request.GET.get('pagina')
    produtos = paginador.get_page(numero_pagina)

    return render(request, 'produtos/listar.html', {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_selecionada': categoria_id,
        'busca': busca,
        'ordenacao': ordenacao
    })



def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        formulario = ProdutoForm(request.POST, instance=produto)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_produtos')

    else:
        formulario = ProdutoForm(instance=produto)

    return render(request, 'produtos/editar.html', {
        'formulario': formulario,
        'produto': produto
    })

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')

    return render(request, 'produtos/excluir.html', {
        'produto': produto
    })