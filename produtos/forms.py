from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = [
            'nome',
            'codigo',
            'descricao',
            'preco',
            'categoria',
            'quantidade',
            'estoque_minimo',
            'ativo',
        ]