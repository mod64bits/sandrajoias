from django import forms
from .models import Venda, Parcelas


class VendaForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = ['valor_total', 'descricao_venda', 'data_compra', 'data_vencimento', 'comprador', 'qtParcelas',
                  'status']





