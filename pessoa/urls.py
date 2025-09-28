from django.urls import path
from . import views

urlpatterns = [
    # Pessoa
    path('pessoas/', views.lista_pessoa, name='lista_pessoa'),
    path('pessoas/adicionar/', views.add_pessoa, name='add_pessoa'),
    path('pessoas/editar/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('pessoas/excluir/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),

    # Funcionario
    path('funcionarios/', views.lista_funcionario, name='lista_funcionario'),
    path('funcionarios/adicionar/', views.add_funcionario, name='add_funcionario'),
    path('funcionarios/editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionarios/excluir/<int:id>/', views.excluir_funcionario, name='excluir_funcionario'),

    # Administrador
    path('administradores/', views.lista_administrador, name='lista_administrador'),
    path('administradores/adicionar/', views.add_administrador, name='add_administrador'),
    path('administradores/editar/<int:id>/', views.editar_administrador, name='editar_administrador'),
    path('administradores/excluir/<int:id>/', views.excluir_administrador, name='excluir_administrador'),

]
