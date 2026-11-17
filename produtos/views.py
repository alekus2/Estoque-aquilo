from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto, Categoria

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

    produtos = Produto.objects.all()

    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)

    return render(request, 'produtos/listar.html', {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_selecionada': categoria_id
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