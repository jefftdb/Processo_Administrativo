from django.db import models

from django.db import models

class Secretaria(models.Model):   
    nome= models.CharField(max_length=100)

    
    def __str__(self):
        return self.nome
    
