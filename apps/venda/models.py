from django.db import models
from apps.core.signals import create_slug
from django.db.models import signals, Sum, F, FloatField
from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from django.urls import reverse


from apps.cliente.models import Cliente
from decimal import Decimal

STATUS = [
    ('andamento', 'Andamento'),
    ('pago', 'Pago'),
]


class Venda(models.Model):
    valor_total = models.DecimalField('Valor Total', max_digits=13, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.00'))], null=True, blank=True)

    descricao_venda = models.TextField('Descrição da Venda')
    data_compra = models.DateField('Data da Compra', default=datetime.now)
    data_vencimento = models.DateField('Data Vencimento', default=datetime.now)
    comprador = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    qtParcelas = models.IntegerField('Quantidade de Parcelas', default=1)
    status = models.CharField(max_length=10, choices=STATUS, default='Andamento')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'descricao_venda'

    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def get_absolute_url(self):
        return reverse('core:home')

    def __str__(self):
        return self.comprador.nome


signals.post_save.connect(create_slug, sender=Venda)


class Parcelas(models.Model):
    descricao = models.CharField('Descricao', max_length=100, null=True, blank=True)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='parcela_vendas')
    valorParcela = models.FloatField(null=True, blank=True)
    pago = models.BooleanField(default=False)
    data_vencimento = models.DateField('Data de Vencimento', null=True, blank=True)
    data_pagamento = models.DateField('Data de Pagamento', null=True, blank=True)
    data = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.descricao
