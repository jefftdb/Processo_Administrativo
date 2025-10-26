from django.db import models
from django.contrib.auth.models import AbstractUser
from secretaria.models import Secretaria
from setor.models import Setor
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Pessoa(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    email = models.CharField(unique=True)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return super().__str__()
    

class Funcionario(Pessoa):
    secretaria = models.ForeignKey(Secretaria,on_delete=models.CASCADE, related_name= 'funcionario_secretaria',null= True)
    setor = models.ForeignKey(Setor,on_delete=models.CASCADE, related_name= 'funcionario_setor',null= True)
    
    def __str__(self):
        return super().__str__()
    
class Administrador(Funcionario):
    def __str__(self):
        return super().__str__()
    



