
from django.contrib import admin
from .models import Produto, Categoria


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nome',
        'codigo',
        'preco',
        'categoria',
        'quantidade',
        'estoque_minimo',
        'ativo',
        'exibir_estoque_baixo'
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
    
    @admin.display(description='Estoque baixo')
    def exibir_estoque_baixo(self, obj):
        return 'Sim' if obj.estoque_baixo else 'Não'
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)