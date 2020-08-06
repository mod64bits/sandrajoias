from django.shortcuts import render
from django.views.generic import TemplateView
from apps.venda.models import Venda, Parcelas
from django.db.models import Sum, F, FloatField
from django.utils.formats import localize

class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todas_vendas'] = Venda.objects.all()
        context['total_de_vendas'] = Venda.objects.all().count()
        context['vendas_abertas'] = Venda.objects.filter(status='andamento').count()
        context['vendas_quitadas'] = Venda.objects.filter(status='pago').count()
        context['valor_total_todas_vendas'] = Venda.objects.all().aggregate(
            tot=Sum(F('valor_total'), output_field=FloatField())
        )['tot']
        return context
