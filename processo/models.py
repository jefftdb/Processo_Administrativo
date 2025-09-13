from django.db import models

class Processo(models.Model):   
    titulo= models.CharField(max_length=100)
    data_criacao= models.DateField()
    data_edicao= models.DateField(null=True)
    descricao= models.TextField()
    
    def __str__(self):
        return self.titulo
    


    