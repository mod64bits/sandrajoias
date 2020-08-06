from django import forms
from .models import Cliente


class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'descricao', 'telefone', 'CPF', 'data_nascimento', 'status']


