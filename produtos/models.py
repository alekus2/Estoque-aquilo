from django.db import models
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=140)
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='produtos'
        )
    quantidade = models.PositiveBigIntegerField(default=5)
    estoque_minimo = models.PositiveBigIntegerField(default=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    
    @property
    def estoque_baixo(self):
        return self.quantidade < self.estoque_minimo
    
    def __str__(self):
        return self.nome
    
    def clean(self):
        if not self.nome or not self.nome.strip():
            raise ValidationError({
                'nome': 'O nome não pode ser vazio.'
            })

        if self.quantidade < 0:
            raise ValidationError({
                'quantidade': 'A quantidade não pode ser negativa.'
            })

        if self.preco < 0:
            raise ValidationError({
                'preco': 'O preço não pode ser negativo.'
            })
    


    