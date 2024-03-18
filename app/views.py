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
    data = request.data
    pessoa_service = PessoaService()

    cpf = data.get('cpf')
    if Pessoa.objects.filter(cpf=cpf).exists():
        return Response({"error": "CPF já cadastrado"}, status=status.HTTP_400_BAD_REQUEST)

    pessoa_service.incluir(data)
    return Response({"message": "Pessoa incluída com sucesso"}, status=status.HTTP_201_CREATED)
    

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
    
    if pessoas.exists():
        # Serializar cada pessoa individualmente e armazenar os resultados em uma lista
        serializer = PessoaSerializer(pessoas, many=True)
        pessoas_serializadas = serializer.data
        return Response(pessoas_serializadas[0])
    else:
        return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def excluir_pessoa(request, pessoa_id):
    pessoa_service = PessoaService()

    pessoa_service.excluir(pessoa_id)
    return Response({"message": "Pessoa excluída com sucesso"}, status=status.HTTP_204_NO_CONTENT)



@api_view(['PUT'])
def atualizar_pessoa(request, pessoa_id):
    pessoa_service = PessoaService()

    try:
        pessoa_service.atualizar(pessoa_id, request.data)
        return Response({"success": "Pessoa atualizada com sucesso"}, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def calcular_peso_ideal(request, pessoa_id):
    pessoa_service = PessoaService()

    pessoa = pessoa_service.obter_pessoa_por_id(pessoa_id)
    print(pessoa)
    if not pessoa:
        return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    altura = pessoa.altura
    # peso = pessoa.peso
    sexo = pessoa.sexo
    
    if sexo == 'M':
        peso_ideal = round((72.7 * altura) - 58, 2)
    elif sexo == 'F':
        peso_ideal = round((62.1 * altura) - 44.7, 2)
    else:
        return Response({"error": "Sexo inválido"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"peso_ideal": peso_ideal, 'nome': pessoa.nome})