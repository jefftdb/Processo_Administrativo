from django.shortcuts import render, redirect, get_object_or_404
from .models import Processo, PessoaProcesso
from pessoa.models import Funcionario
from django.contrib import messages
from datetime import date

def listar_processos(request):
    processos = Processo.objects.all()
    return render(request, 'processo/lista_processos.html', {'processos': processos})

def adicionar_processo(request):
    funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        funcionario_id = request.POST['funcionario']
        funcionario = Funcionario.objects.get(id = funcionario_id)
        
        processo = Processo.objects.create(
            titulo=titulo,
            descricao=descricao
        )

        pessoaProcesso = PessoaProcesso.objects.create(
            codigo = "",
            pessoa=funcionario,
            processo=processo,
            data = date.today()
        )
        pessoaProcesso.gerar_codigo_unico(),
        messages.success(request, "Processo adicionado com sucesso!")
        return redirect('lista_processos')

    return render(request, 'processo/adicionar_processo.html', {'funcionarios': funcionarios})

def editar_processo(request, id):
    processo = get_object_or_404(Processo, id=id)
    funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        processo.titulo = request.POST['titulo']
        processo.descricao = request.POST['descricao']
        processo.data_edicao = date.today()
        processo.save()
        messages.success(request, "Processo atualizado com sucesso!")
        return redirect('lista_processos')
    return render(request, 'processo/editar_processo.html', {'processo': processo,'funcionarios': funcionarios})

def excluir_processo(request, id):
    processo = get_object_or_404(Processo, id=id)
    processo.delete()
    messages.success(request, "Processo excluído com sucesso!")
    return redirect('lista_processos')

def detalhe_processo(request, id):
    processo = get_object_or_404(Processo, id=id)
    pessoaProcesso = get_object_or_404(PessoaProcesso,processo = processo)
    return render(request, 'processo/detalhe_processo.html', {'processo': processo, 'pessoaProcesso' : pessoaProcesso})