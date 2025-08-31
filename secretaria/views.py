from django.shortcuts import render,HttpResponse
from secretaria.models import Secretaria

def vizualizarSecretaria(request):
    secretaria = Secretaria()
    secretaria.nome = "primeira Secretaria"
    
    return HttpResponse(secretaria.__str__())
