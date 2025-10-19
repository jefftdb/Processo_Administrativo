from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Pessoa
    path('', views.lista_pessoa, name='lista_pessoa'),
    path('adicionar/', views.add_pessoa, name='add_pessoa'),
    path('editar/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('excluir/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),

    # Funcionario
    path('funcionarios/', views.lista_funcionario, name='lista_funcionario'),
    path('funcionarios/adicionar/', views.add_funcionario, name='add_funcionario'),
    path('funcionarios/editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionarios/excluir/<int:id>/', views.excluir_funcionario, name='excluir_funcionario'),
    path('buscar-funcionarios/', views.buscar_funcionarios, name='buscar_funcionarios'),

    # Administrador
    path('administradores/', views.lista_administrador, name='lista_administrador'),
    path('administradores/adicionar/', views.add_administrador, name='add_administrador'),
    path('administradores/editar/<int:id>/', views.editar_administrador, name='editar_administrador'),
    path('administradores/excluir/<int:id>/', views.excluir_administrador, name='excluir_administrador'),

]
