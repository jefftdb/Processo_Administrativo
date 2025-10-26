from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pessoa, Funcionario, Administrador
from .forms import PessoaForm, FuncionarioForm, AdministradorForm
from django.contrib.auth.models import Group
from django.http import JsonResponse


# ---------------------- PESSOA ----------------------
def lista_pessoa(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa/lista_pessoa.html', {'pessoas': pessoas})


def add_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.set_password(form.cleaned_data['password'])  # senha criptografada
            pessoa.save()

            # Adicionar ao grupo "Pessoa"
            grupo = Group.objects.get(name="Pessoa")
            pessoa.groups.add(grupo)

            messages.success(request, "Pessoa adicionada com sucesso!")
            return redirect('login')
    else:
        form = PessoaForm()
    return render(request, 'pessoa/add_pessoa.html', {'form': form})


def editar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa = form.save(commit=False)
            if form.cleaned_data['password']:
                pessoa.set_password(form.cleaned_data['password'])
            pessoa.save()
            messages.success(request, "Pessoa atualizada com sucesso!")
            return redirect('login')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoa/editar_pessoa.html', {'form': form, 'pessoa': pessoa})

def excluir_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()
    messages.success(request, "Pessoa excluída com sucesso!")
    return redirect('lista_pessoa')


# ---------------------- FUNCIONARIO ----------------------

def buscar_funcionarios(request):
    termo = request.GET.get('q', '')
    funcionarios = Funcionario.objects.filter(username__icontains=termo)[:10]
    data = [{'id': f.id, 'username': f.username} for f in funcionarios]
    return JsonResponse(data, safe=False)

def lista_funcionario(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/lista_funcionario.html', {'funcionarios': funcionarios})

def add_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.set_password(form.cleaned_data['password'])
            funcionario.save()

            # Adicionar ao grupo "Funcionario"
            grupo = Group.objects.get(name="Funcionario")
            funcionario.groups.add(grupo)

            messages.success(request, "Funcionário adicionado com sucesso!")
            return redirect('lista_funcionario')
    else:
        form = FuncionarioForm()
    return render(request, 'funcionario/add_funcionario.html', {'form': form})


def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            funcionario = form.save(commit=False)
            if form.cleaned_data['password']:
                funcionario.set_password(form.cleaned_data['password'])
            funcionario.save()
            messages.success(request, "Funcionário atualizado com sucesso!")
            return redirect('lista_funcionario')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'funcionario/editar_funcionario.html', {'form': form, 'funcionario': funcionario})

def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()
    messages.success(request, "Funcionário excluído com sucesso!")
    return redirect('lista_funcionario')


# ---------------------- ADMINISTRADOR ----------------------
def lista_administrador(request):
    administradores = Administrador.objects.all()
    return render(request, 'administrador/lista_administrador.html', {'administradores': administradores})

def add_administrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.set_password(form.cleaned_data['password'])
            admin.save()

            # Adicionar ao grupo "Administrador"
            grupo = Group.objects.get(name="Administrador")
            admin.groups.add(grupo)

            messages.success(request, "Administrador adicionado com sucesso!")
            return redirect('lista_administrador')
    else:
        form = AdministradorForm()
    return render(request, 'administrador/add_administrador.html', {'form': form})


def editar_administrador(request, id):
    admin = get_object_or_404(Administrador, id=id)
    if request.method == 'POST':
        form = AdministradorForm(request.POST, instance=admin)
        if form.is_valid():
            admin = form.save(commit=False)
            if form.cleaned_data['password']:
                admin.set_password(form.cleaned_data['password'])
            admin.save()
            messages.success(request, "Administrador atualizado com sucesso!")
            return redirect('lista_administrador')
    else:
        form = AdministradorForm(instance=admin)
    return render(request, 'administrador/editar_administrador.html', {'form': form, 'administrador': admin})

def excluir_administrador(request, id):
    admin = get_object_or_404(Administrador, id=id)
    admin.delete()
    messages.success(request, "Administrador excluído com sucesso!")
    return redirect('lista_administrador')


