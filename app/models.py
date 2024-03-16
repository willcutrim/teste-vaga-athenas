from django.db import models

class Pessoa(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    altura = models.FloatField()
    peso = models.FloatField()

    def __str__(self):
        return self.nome


    def data_formatada(self):
        return self.data_nasc.strftime('%d/%m/%Y')
    

    def sexo_formatado(self):
        return self.get_sexo_display()
    

    def altura_formatada(self):
        return f'{self.altura:.2f}'

    
    def peso_formatado(self):
        return f'{self.peso:.2f}'
    

    def cpf_formatado(self):
        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'