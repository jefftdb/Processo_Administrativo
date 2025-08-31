from django.db import models
from django.contrib.auth.models import AbstractUser

class Pessoa(AbstractUser):
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return super().__str__()
    
    def VisualizarProcesso(self):
        return "Todos os processos"
    
    def VisualizaPerfil(self):
        return "Meu perfil"