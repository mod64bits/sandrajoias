from django.urls import path
from .views import HomeView
from apps.venda.views import NovaVendaView, VendaDetalheView, PagarParcelaView


app_name = 'core'

urlpatterns = [
    path('pagar/<int:pk>/', PagarParcelaView.as_view(), name='pagar-parcela'),
    path('venda/<slug:slug>/', VendaDetalheView.as_view(), name='detalhe-venda'),
    path('nova/venda', NovaVendaView.as_view(), name='nova-venda'),
    path('', HomeView.as_view(), name='home'),
]
