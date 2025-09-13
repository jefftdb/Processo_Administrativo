from django.shortcuts import render,HttpResponse
from processo.models import Processo
from django.contrib import messages
from datetime import datetime

def vizualizarProcesso(request):
    processo = Processo()
    processo.titulo = "primeiro teste"
    processo.descricao = 'primiro teste concluido'
    
    return HttpResponse(f"Titulo = {processo.titulo}  Descrição={processo.descricao}")

def add_processo(request):
    
    if request.method == 'POST':
        titulo= request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_criacao = datetime.now()
        
        Processo.objects.create(titulo=titulo,descricao =descricao,data_criacao=data_criacao)
        messages.success(request, "Processo adicionada com sucesso!")
    
        return HttpResponse(messages)
    return render(request,'processo/add_processo.html')