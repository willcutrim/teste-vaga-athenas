from .models import Pessoa


from .models import Pessoa

class PessoaService:
    def incluir(self, data):
        nome = data.get('nome')
        data_nasc = data.get('data_nasc')
        cpf = data.get('cpf')
        sexo = data.get('sexo')
        altura = data.get('altura')
        peso = data.get('peso')
        
        pessoa = Pessoa.objects.create(
            nome=nome,
            data_nasc=data_nasc,
            cpf=cpf,
            sexo=sexo,
            altura=altura,
            peso=peso
        )

    
    def excluir(self, pessoa_id):
        pessoa = Pessoa.objects.get(id=pessoa_id)
        pessoa.delete()




    def atualizar(self, pessoa_id, data):
        try:
            pessoa = Pessoa.objects.get(id=pessoa_id)
        except Pessoa.DoesNotExist:
            raise ValueError("Pessoa não encontrada")

        pessoa.nome = data.get('nome', pessoa.nome)
        pessoa.data_nasc = data.get('data_nasc', pessoa.data_nasc)
        pessoa.cpf = data.get('cpf', pessoa.cpf)
        pessoa.sexo = data.get('sexo', pessoa.sexo)
        pessoa.altura = data.get('altura', pessoa.altura)
        pessoa.peso = data.get('peso', pessoa.peso)

        # Salva as alterações no banco de dados
        pessoa.save()

    
    def obter_pessoa_por_id(self, pessoa_id):
        try:
            return Pessoa.objects.get(id=pessoa_id)
        except Pessoa.DoesNotExist:
            raise ValueError("Pessoa não encontrada")

