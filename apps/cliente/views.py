from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import date

from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import ListView
from .forms import ClientForm
from .models import Cliente
from apps.venda.models import Venda, Parcelas


class NovoClienteView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ClientForm
    template_name = 'cliente/NovoCliente.html'
    success_message = "%(nome)s Cadastrado com Sucesso"


class TodosClientesView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Cliente
    context_object_name = 'Lista_de_Clientes'
    template_name = 'cliente/ListaClientes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ativos'] = Cliente.objects.filter(status='ativo').count
        context['inativos'] = Cliente.objects.filter(status='inativo').count
        context['totalClientes'] = Cliente.objects.all().count
        context['aniversariantesDoDia'] =  aniv = Cliente.objects.filter(
            data_nascimento__day=date.today().day, data_nascimento__month=date.today().month).count
        return context


class ExcluirClienteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cliente
    success_message = "%(nome)s  Excluido com Sucesso!!"
    success_url = reverse_lazy('cliente:lista-cliente')


class DetalheClienteView(LoginRequiredMixin, DetailView):
    model = Cliente
    context_object_name = 'clienteDetalhe'
    template_name = 'cliente/ClienteDetalhe.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        parce = Parcelas.objects.filter(venda=self.object.id)
        context = super().get_context_data(**kwargs)
        context['compras'] = Venda.objects.filter(comprador=self.object.id)
        context['parcelas'] = parce

        return context


class EditarClienteView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/EditarCliente.html'
    success_message = "%(nome)s  Editado com Sucesso!!"





















