from django.urls import path
from .views import HomeView
from apps.venda.views import NovaVendaView, VendaDetalheView


app_name = 'core'

urlpatterns = [
    path('venda/<slug:slug>/', VendaDetalheView.as_view(), name='detalhe-venda'),
    path('nova/venda', NovaVendaView.as_view(), name='nova-venda'),
    path('', HomeView.as_view(), name='home'),

]
