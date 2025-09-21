from django.db import models
from django.contrib.auth.models import AbstractUser
from secretaria.models import Secretaria
from processo.models import Processo
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
import random
import string



class Pessoa(AbstractUser):
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return super().__str__()
    

class Funcionario(Pessoa):
    secretaria = models.ForeignKey(Secretaria,on_delete=models.CASCADE, related_name= 'funcionario_secretaria',null=True)
    def __str__(self):
        return super().__str__()
    
class Administrador(Funcionario):
    def __str__(self):
        return super().__str__()
    
class PessoaProcesso(models.Model):
    codigo = models.CharField(max_length=6)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    
    def gerar_codigo_unico(self):
        while True:
            letras = ''.join(random.choices(string.ascii_uppercase, k=3))
            numeros = ''.join(random.choices(string.digits, k=3))
            codigo = letras + numeros 
            
            if not PessoaProcesso.objects.filter(codigo=codigo).exists():
                return codigo

    def __str__(self):
        return f"{self.processo} -> {self.pessoa} ({self.data})"



Processo.pessoas = models.ManyToManyField(Pessoa, through=PessoaProcesso, related_name="processos")


