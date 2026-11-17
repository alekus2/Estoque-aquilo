from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=140)
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveBigIntegerField(default=5)
    estoque_minimo = models.PositiveBigIntegerField(default=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome