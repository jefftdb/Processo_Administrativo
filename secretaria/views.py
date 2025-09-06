from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Secretaria

def add_secretaria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')        
       
        if not nome:
            messages.error(request, "O nome da secretaria é obrigatório.")
            return redirect('add_secretaria')

    
        if Secretaria.objects.filter(nome__iexact=nome).exists():
            messages.warning(request, "Já existe uma secretaria com esse nome.")
            return redirect('add_secretaria')

       
        Secretaria.objects.create(nome=nome)
        messages.success(request, "Secretaria adicionada com sucesso!")
        return redirect('lista_secretaria') 

    return render(request, 'secretaria/add_secretaria.html')

def lista_secretaria(request):
    lista= Secretaria.objects.all()
  
    
    return render(request, 'secretaria/lista_secretaria.html', {'lista': lista})

def excluir_secretaria(request,id):
    
    secretaria = get_object_or_404(Secretaria, id=id) 
    secretaria.delete() 
    messages.success(request, "Secretaria deletada com sucesso!")
    return redirect('lista_secretaria')

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