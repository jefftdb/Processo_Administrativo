from django.shortcuts import render,HttpResponse
from processo.models import Processo

def vizualizarProcesso(request):
    processo = Processo()
    processo.titulo = "primeiro teste"
    processo.descricao = 'primiro teste concluido'
    
    return HttpResponse(f"Titulo = {processo.titulo}  Descrição={processo.descricao}")