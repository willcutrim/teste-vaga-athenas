from django.test import TestCase, Client
from rest_framework import status
from .models import Pessoa
from .serializers import PessoaSerializer
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.incluir_url = '/incluir/'
        self.listar_pessoas_url = '/listar_pessoas/'
        self.obter_pessoa_url = '/obter_pessoa/'
        self.excluir_pessoa_url = '/excluir_pessoa/{}/'
        self.atualizar_pessoa_url = '/atualizar_pessoa/{}/'
        self.calcular_peso_ideal_url = '/calcular_peso_ideal/{}/'
        self.pessoa_data = {
            'nome': 'Teste',
            'cpf': '12345678901',
            'altura': 1.75,
            'peso': 70,
            'sexo': 'M'
        }
        self.pessoa = Pessoa.objects.create(**self.pessoa_data)

    def test_incluir_view(self):
        """Teste para verificar se a view de inclusão de pessoa funciona corretamente."""
        response = self.client.post(self.incluir_url, data=json.dumps(self.pessoa_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_pessoas_view(self):
        """Teste para verificar se a view de listagem de pessoas funciona corretamente."""
        response = self.client.get(self.listar_pessoas_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_obter_pessoa_view(self):
        """Teste para verificar se a view de obtenção de pessoa funciona corretamente."""
        response = self.client.get(self.obter_pessoa_url, {'data': 'Teste'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_excluir_pessoa_view(self):
        """Teste para verificar se a view de exclusão de pessoa funciona corretamente."""
        response = self.client.delete(self.excluir_pessoa_url.format(self.pessoa.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_atualizar_pessoa_view(self):
        """Teste para verificar se a view de atualização de pessoa funciona corretamente."""
        updated_data = {
            'nome': 'Teste Atualizado',
            'cpf': '12345678901',
            'altura': 1.75,
            'peso': 75,
            'sexo': 'M'
        }
        response = self.client.put(self.atualizar_pessoa_url.format(self.pessoa.id), data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_calcular_peso_ideal_view(self):
        """Teste para verificar se a view de cálculo de peso ideal funciona corretamente."""
        response = self.client.get(self.calcular_peso_ideal_url.format(self.pessoa.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
