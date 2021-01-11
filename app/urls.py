from django.urls import path
from app.views import *

urlpatterns = [
    path('proprietarios/<int:cpf>',
    RetrieveProprietarioView.as_view(), name='proprietarios'),
    path('veiculos/<str:placa>',
    RetrieveVeiculoView.as_view(), name='veiculos'),
    path('proprietarios/<int:cpf>/veiculos',
    ListProprietarioVeiculo.as_view(), name='proprietario_veiculos')
]

