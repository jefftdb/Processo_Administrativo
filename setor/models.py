from django.db import models
from pessoa.models import Funcionario

class Setor(models.Model):
    nome = models.CharField(max_length=25)
    funcionarios = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="funcionario_setor")

    def __str__(self):
        return self.nome