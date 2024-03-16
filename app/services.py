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


