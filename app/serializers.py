from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import *

class ProprietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'
