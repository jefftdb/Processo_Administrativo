from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Endereco
from .forms import EnderecoForm

@login_required
def lista_endereco(request):
    enderecos = Endereco.objects.all()
    return render(request, 'endereco/lista_endereco.html', {'enderecos': enderecos})

@login_required
def add_endereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Endereço adicionado com sucesso!")
            return redirect('lista_endereco')
    else:
        form = EnderecoForm()
    return render(request, 'endereco/add_endereco.html', {'form': form})

@login_required
def editar_endereco(request, id):
    endereco = get_object_or_404(Endereco, id=id)
    if request.method == 'POST':
        form = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            form.save()
            messages.success(request, "Endereço atualizado com sucesso!")
            return redirect('lista_endereco')
    else:
        form = EnderecoForm(instance=endereco)
    return render(request, 'endereco/editar_endereco.html', {'form': form, 'endereco': endereco})

@login_required
def excluir_endereco(request, id):
    endereco = get_object_or_404(Endereco, id=id)
    endereco.delete()
    messages.success(request, "Endereço excluído com sucesso!")
    return redirect('lista_endereco')
