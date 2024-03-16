from django.db.models import Q

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import Pessoa
from .services import PessoaService
from .serializers import PessoaSerializer



def index(request):
    return render(request, 'html/index.html')


@api_view(['POST'])
def incluir(request):
    if request.method == 'POST':
        data = request.data

        # Verificar se o CPF já existe
        cpf = data.get('cpf')
        if Pessoa.objects.filter(cpf=cpf).exists():
            return Response({"error": "CPF já cadastrado"}, status=status.HTTP_400_BAD_REQUEST)

        # Se o CPF não existir, prosseguir com a inclusão
        pessoa_service = PessoaService()
        pessoa_service.incluir(data)
        return Response({"message": "Pessoa incluída com sucesso"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def listar_pessoas(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        serialized_pessoas = PessoaSerializer(pessoas, many=True)
        return Response(serialized_pessoas.data)
    else:
        return Response({"error": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def obter_pessoa(request):
    termo_busca = request.GET.get('data', '')
    # Buscar pessoas com base no termo de busca
    pessoas = Pessoa.objects.filter(
        Q(nome=termo_busca) | 
        Q(cpf=termo_busca)
    )
    
    # Verificar se foi encontrada pelo menos uma pessoa
    if pessoas.exists():
        # Serializar cada pessoa individualmente e armazenar os resultados em uma lista
        serializer = PessoaSerializer(pessoas, many=True)
        pessoas_serializadas = serializer.data
        return Response(pessoas_serializadas[0])
    else:
        return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def excluir_pessoa(request, pessoa_id):
    try:
        pessoa = Pessoa.objects.get(pk=pessoa_id)
    except Pessoa.DoesNotExist:
        return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    pessoa.delete()
    return Response({"message": "Pessoa excluída com sucesso"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def atualizar_pessoa(request, pessoa_id):
    try:
        pessoa = Pessoa.objects.get(pk=pessoa_id)
    except Pessoa.DoesNotExist:
        return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PessoaSerializer(pessoa, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def calcular_peso_ideal(request, pessoa_id):
    
    try:
        pessoa = Pessoa.objects.get(id=pessoa_id)
        
    except Pessoa.DoesNotExist:
        return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    altura = pessoa.altura
    peso = pessoa.peso
    sexo = pessoa.sexo
    
    if sexo == 'M':
        peso_ideal = round((peso * altura) - 58, 2)
    elif sexo == 'F':
        peso_ideal = round((peso * altura) - 44.7, 2)
    else:
        return Response({"error": "Sexo inválido"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"peso_ideal": peso_ideal, 'nome': pessoa.nome})