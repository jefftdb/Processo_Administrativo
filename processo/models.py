from django.db import models

class Processo(models.Model):   
    titulo= models.CharField(max_length=100)
    data_criacao= models.DateField()
    data_edicao= models.DateField()
    descricao= models.CharField(max_length=255)
    
    def __str__(self):
        return self.titulo
    
    def EditarProcesso(self):
        return "editar Processo"
    
    def InserirProcesso(self):
        return "inserir processo"
    
    def ExcluirProcesso(self):
        return "Excluir processo"
    
    def VizualizarProcesso(self):
        return "Vizualizar processo"

    