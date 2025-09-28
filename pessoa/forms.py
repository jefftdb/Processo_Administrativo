from django import forms
from .models import Pessoa, Funcionario, Administrador

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['first_name','last_name','username', 'email', 'cpf', 'telefone', 'password']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['first_name','last_name','username', 'email', 'cpf', 'telefone', 'password', 'secretaria']

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['first_name','last_name','username', 'email', 'cpf', 'telefone', 'password', 'secretaria']

