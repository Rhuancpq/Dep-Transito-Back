from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import permissions
from app.models import *
from app.serializers import *

class ListProprietarioView(generics.ListAPIView):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer
    lookup_field = 'cpf'

class RetrieveProprietarioView(generics.RetrieveAPIView):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer
    lookup_field = 'cpf'

class ListVeiculoView(generics.ListAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    lookup_field = 'placa'

class RetrieveVeiculoView(generics.RetrieveAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    lookup_field = 'placa'

class ListProprietarioVeiculo(generics.ListAPIView):
    serializer_class = VeiculoSerializer
    def get_queryset(self):
        cpf = self.kwargs['cpf']
        return Veiculo.objects.filter(proprietario__cpf=cpf)
    
    
