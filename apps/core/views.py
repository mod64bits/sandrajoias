from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.venda.models import Venda, Parcelas
from django.db.models import Sum, F, FloatField
from django.utils.formats import localize

from apps.cliente.models import Cliente
from datetime import date


class HomeView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/index.html'

    def aniversariantes(self, **kwargs):

        aniv = Cliente.objects.filter(data_nascimento__day=date.today().day, data_nascimento__month=date.today().month)
        return aniv


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todas_vendas'] = Venda.objects.all()
        context['total_de_vendas'] = Venda.objects.all().count()
        context['vendas_abertas'] = Venda.objects.filter(status='andamento').count()
        context['vendas_quitadas'] = Venda.objects.filter(status='pago').count()
        context['aniversarios'] = self.aniversariantes()
        context['valor_total_todas_vendas'] = Venda.objects.all().aggregate(
            tot=Sum(F('valor_total'), output_field=FloatField())
        )['tot']
        return context
