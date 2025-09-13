from django.db import models
from pessoa.models import Funcionario
from secretaria.models import Secretaria

class Endereco(models.Model):
    
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    pais = models.CharField(max_length=20)
    numero =models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE,related_name="endereco_funcionario")
    secretaria = models.ForeignKey(Secretaria,on_delete=models.CASCADE,related_name="endereco_secretaria")

    def __str__(self):
        return f'Endereço de {self.funcionario.first_name}'