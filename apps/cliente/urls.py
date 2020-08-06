from django.urls import path
from .views import NovoClienteView, TodosClientesView, ExcluirClienteView, DetalheClienteView, EditarClienteView


app_name = 'cliente'


urlpatterns = [
    path('editar/<slug:slug>/', EditarClienteView.as_view(), name='editar-cliente'),
    path('detalhe/<slug:slug>/', DetalheClienteView.as_view(), name='detalhe-cliente'),
    path('excluir/<slug:slug>/', ExcluirClienteView.as_view(), name='excluir-cliente'),
    path('', TodosClientesView.as_view(), name='lista-cliente'),
    path('novo/', NovoClienteView.as_view(), name='novo-cliente'),

]
