from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date
from django.utils import timezone
from dateutil.relativedelta import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .forms import VendaForm
from .models import Venda, Parcelas


class NovaVendaView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = VendaForm
    template_name = 'venda/NovaVenda.html'

    # success_message = "Nova Venda Realizada com Sucesso!!"

    def post(self, request, *args, **kwargs):
        form = VendaForm(request.POST)  # obtendo uma estancia do venda form
        valor = float(float(request.POST['valor_total']) / int(
            request.POST['qtParcelas']))  # pegando as informacoes na request e convertendo os valores
        NOW = date.today()  # pegando data atual
        if form.is_valid():  # Verificando se o form é valido
            cont = 0
            quantParcelas = int(request.POST['qtParcelas'])
            descricao_parcela = (str(request.POST['data_compra']))

            p = form.save()  # salvando o form
            venda = Venda.objects.last()  # pegando a venda que foi salva
            qt = int(request.POST['qtParcelas'])
            if qt > 1:  # verifico se é mais que uma parcela
                while qt >= 1:  # laço para gerar as parcelas
                    cont += 1
                    # criando as parcelas
                    parc = Parcelas.objects.create(
                        descricao=str(cont) + "-" + 'de' + '' + str(quantParcelas) + '-' + descricao_parcela,
                        # usando a biblioteca relativedelta para fazer calculo de data nesse caso mes a mes
                        venda=venda, valorParcela=valor, data_vencimento=NOW + relativedelta(months=+cont))
                    parc.save()
                    qt -= 1
            else:
                parc = Parcelas.objects.create(descricao='1-' + descricao_parcela, venda=venda,
                                               valorParcela=valor)
                parc.save()
            p.save()
            return HttpResponseRedirect(reverse_lazy('core:home'))

        return render(request, 'venda/NovaVenda.html', {'form': form})

    success_message = "Nova Venda Realizada com Sucesso!!"


class PagarParcelaView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Parcelas
    template_name = 'venda/PagarParcela.html'
    fields = ['data_pagamento', 'pago']


class VendaDetalheView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Venda
    template_name = 'venda/VendaDetalhe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['compras'] = Venda.objects.filter(comprador=self.object.id)
        context['parcelas'] = Parcelas.objects.filter(venda=self.object.id)

        return context


class VencimentosView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Parcelas
    template_name = 'venda/PagarParcela.html'

    def get_queryset(self):
        VencimentoHoje = date.today()
        context = {}
        context['hoje'] = Parcelas.objects.filter(data_vencimento=VencimentoHoje)
        context['esse_mes'] = Parcelas.objects.filter(data_vencimento=VencimentoHoje + relativedelta(months=+1))
        return context
