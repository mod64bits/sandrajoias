from django.db import models
from apps.core.signals import create_slug
from django.db.models import signals
from django.urls import reverse


STATUS = (
        ('ativo','ATIVO'),
        ('inativo','INATIVO'),

    )


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    endereco = models.CharField('Endereço', max_length=255)
    descricao = models.TextField('Descrição')
    telefone = models.CharField(max_length=32)
    CPF = models.CharField('CPF', max_length=11, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    status = models.CharField('Estatus',
        max_length=7,
        choices=STATUS,
    )
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def get_absolute_url(self):
        return reverse('cliente:lista-cliente')

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug, sender=Cliente)

