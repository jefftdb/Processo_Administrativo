from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Processo, PessoaProcesso
from pessoa.models import Funcionario
from django.contrib import messages
from datetime import date
from django.core.paginator import Paginator
from django.db.models import Q, Max
from django.shortcuts import render
from .models import PessoaProcesso


def home(request):
    return render(request, 'home.html')

@login_required
def listar_processos(request):
    # Base inicial: últimos registros de cada processo
    processos_query = (
        PessoaProcesso.objects
        .values('processo')
        .annotate(ultimo_id=Max('id'))
    )
    ids = [p['ultimo_id'] for p in processos_query]
    processos = PessoaProcesso.objects.filter(id__in=ids)

    # Filtro de pesquisa
    if request.method == "POST":
        palavra = request.POST.get("palavra", "").strip()
        if palavra:
            # Aplica o filtro e mantém só o último de cada processo
            processos_filtrados = PessoaProcesso.objects.filter(
                Q(processo__titulo__icontains=palavra) |
                Q(codigo__icontains=palavra)
            ).values('processo').annotate(ultimo_id=Max('id'))

            ids_filtrados = [p['ultimo_id'] for p in processos_filtrados]
            processos = PessoaProcesso.objects.filter(id__in=ids_filtrados)

    # Paginação
    paginator = Paginator(processos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'processo/lista_processos.html', {'page_obj': page_obj})

@login_required
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
            data_inicio = date.today()
        )
        pessoaProcesso.gerar_codigo_unico(),
        messages.success(request, "Processo adicionado com sucesso!")
        return redirect('lista_processos')

    return render(request, 'processo/adicionar_processo.html', {'funcionarios': funcionarios})

@login_required
def editar_processo(request, id):
    processo = get_object_or_404(Processo, id=id)    
    funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        pessoaProcesso = PessoaProcesso.objects.filter(processo=processo).order_by('id').last()
        pessoaProcesso.data_termino = date.today()
        pessoaProcesso.save()
                    
        funcionario_id = request.POST['funcionario']
        funcionario = Funcionario.objects.get(id = funcionario_id)
        
        processo.titulo = request.POST['titulo']
        processo.descricao = request.POST['descricao']        
        processo.data_edicao = date.today()
        processo.save()
         
        
        
        PessoaProcesso.objects.create(
            codigo = pessoaProcesso.codigo,
            pessoa=funcionario,
            processo=processo,
            data_inicio = date.today(),
        )
        messages.success(request, "Processo atualizado com sucesso!")
        return redirect('lista_processos')
    return render(request, 'processo/editar_processo.html', {'processo': processo,'funcionarios': funcionarios})

@login_required
def excluir_processo(request, id):
    processo = get_object_or_404(Processo, id=id)
    processo.delete()
    messages.success(request, "Processo excluído com sucesso!")
    return redirect('lista_processos')

@login_required
def detalhe_processo(request, id):
    processo = get_object_or_404(Processo, id=id)
    pessoaProcesso = PessoaProcesso.objects.filter(processo = processo)
    return render(request, 'processo/detalhe_processo.html', {'processo': processo, 'pessoaProcesso' : pessoaProcesso})

