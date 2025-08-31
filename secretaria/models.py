from django.db import models

from django.db import models

class Secretaria(models.Model):   
    nome= models.CharField(max_length=100)

    
    def __str__(self):
        return self.nome
    
    def EditarSecretaria(self):
        return "editar Secretaria"
    
    def InserirSecretaria(self):
        return "inserir Secretaria"
    
    def ExcluirSecretaria(self):
        return "Excluir Secretaria"
    
    def VizualizarSecretaria(self):
        return "Vizualizar Secretaria"