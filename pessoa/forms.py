from django import forms
from .models import Pessoa, Funcionario, Administrador

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['first_name', 'last_name', 'username', 'email', 'cpf', 'telefone', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['first_name', 'last_name', 'username', 'email', 'cpf', 'telefone', 'password', 'secretaria']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'secretaria': forms.Select(attrs={'class': 'form-control'}),
        }

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['first_name', 'last_name', 'username', 'email', 'cpf', 'telefone', 'password', 'secretaria']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'secretaria': forms.Select(attrs={'class': 'form-control'}),
        }
