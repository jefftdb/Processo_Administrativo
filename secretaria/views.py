from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Secretaria

from django.http import JsonResponse
from django.contrib import messages
from .models import Secretaria

@login_required
def add_secretaria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()

        if not nome:
            return JsonResponse({'status': 'error', 'message': 'O nome da secretaria é obrigatório.'})

        if Secretaria.objects.filter(nome__iexact=nome).exists():
            return JsonResponse({'status': 'warning', 'message': 'Já existe uma secretaria com esse nome.'})

        secretaria = Secretaria.objects.create(nome=nome)
        return JsonResponse({
            'status': 'success',
            'message': 'Secretaria adicionada com sucesso!',
            'id': secretaria.id,
            'nome': secretaria.nome
        })

    return JsonResponse({'status': 'error', 'message': 'Método inválido.'})

@login_required
def lista_secretaria(request):
    lista= Secretaria.objects.all()
  
    
    return render(request, 'secretaria/lista_secretaria.html', {'lista': lista})

@login_required
def excluir_secretaria(request,id):
    
    secretaria = get_object_or_404(Secretaria, id=id) 
    secretaria.delete() 
    messages.success(request, "Secretaria deletada com sucesso!")
    return redirect('lista_secretaria')

@login_required
def editar_secretaria(request,id):
    
    secretaria = get_object_or_404(Secretaria, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
    
        if not nome:
            messages.error(request, "O nome da secretaria é obrigatório.")
            return redirect('editar_secretaria', id=id)

        if Secretaria.objects.filter(nome__iexact=nome).exclude(id=id).exists():
            messages.warning(request, "Já existe uma secretaria com esse nome.")
            return redirect('editar_secretaria', id=id)

        
        secretaria.nome = nome
        secretaria.save()

        messages.success(request, "Secretaria atualizada com sucesso!")
        return redirect('lista_secretaria')

    
    return render(request, 'secretaria/editar_secretaria.html', {'secretaria': secretaria})