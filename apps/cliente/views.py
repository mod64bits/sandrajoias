from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils import timezone

from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import ListView
from .forms import ClientForm
from .models import Cliente
from apps.venda.models import Venda, Parcelas


class NovoClienteView(SuccessMessageMixin, CreateView):
    form_class = ClientForm
    template_name = 'cliente/NovoCliente.html'
    success_message = "%(nome)s Cadastrado com Sucesso"


class TodosClientesView(ListView):
    model = Cliente
    context_object_name = 'Lista_de_Clientes'
    template_name = 'cliente/ListaClientes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ativos'] = Cliente.objects.filter(status='ativo').count
        context['inativos'] = Cliente.objects.filter(status='inativo').count
        context['totalClientes'] = Cliente.objects.all().count
        return context


class ExcluirClienteView(DeleteView):
    model = Cliente
    success_message = "%(nome)s  Excluido com Sucesso!!"
    success_url = reverse_lazy('cliente:lista-cliente')


class DetalheClienteView(DetailView):
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


class EditarClienteView(SuccessMessageMixin, UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/EditarCliente.html'
    success_message = "%(nome)s  Editado com Sucesso!!"





















