
from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nome',
        'codigo',
        'preco',
        'quantidade',
        'estoque_minimo',
        'ativo',
    )

    list_display_links = ('id', 'nome')

    list_editable = ('quantidade',)

    search_fields = ('nome', 'codigo', 'descricao')

    list_filter = ('ativo', 'criado_em')

    ordering = ('nome',)

    fieldsets = (
        ('Informações do produto', {
            'fields': ('nome', 'codigo', 'descricao')
        }),
        ('Valores e estoque', {
            'fields': ('preco', 'quantidade', 'estoque_minimo')
        }),
        ('Controle', {
            'fields': (
                'ativo',
                'criado_em',
                'atualizado_em',
            )
        })
    )

    readonly_fields = ('criado_em', 'atualizado_em')
