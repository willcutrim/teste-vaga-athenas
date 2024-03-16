from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'data_formatada', 'cpf_formatado', 'cpf', 'sexo', 'data_nasc', 'sexo_formatado', 'altura_formatada', 'peso_formatado']
