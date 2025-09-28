from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Setor
from setor.forms import SetorForm 

# Lista setores
def lista_setor(request):
    setores = Setor.objects.all()
    return render(request, 'setor/lista_setor.html', {'setores': setores})

# Adiciona setor
def add_setor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Setor adicionado com sucesso!")
            return redirect('lista_setor')
    else:
        form = SetorForm()
    return render(request, 'setor/add_setor.html', {'form': form})

# Edita setor
def editar_setor(request, id):
    setor = get_object_or_404(Setor, id=id)
    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            messages.success(request, "Setor atualizado com sucesso!")
            return redirect('lista_setor')
    else:
        form = SetorForm(instance=setor)
    return render(request, 'setor/editar_setor.html', {'form': form, 'setor': setor})

# Exclui setor
def excluir_setor(request, id):
    setor = get_object_or_404(Setor, id=id)
    setor.delete()
    messages.success(request, "Setor excluído com sucesso!")
    return redirect('lista_setor')
