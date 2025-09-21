from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_pessoa_processos, name="listar_pessoa_processos"),
    path("<int:id>/", views.visualizar_pessoa_processo, name="visualizar_pessoa_processo"),
    path("criar/", views.criar_pessoa_processo, name="criar_pessoa_processo"),
    path("<int:id>/editar/", views.editar_pessoa_processo, name="editar_pessoa_processo"),
    path("<int:id>/excluir/", views.excluir_pessoa_processo, name="excluir_pessoa_processo"),
    path("criar_pessoa",views.criar_pessoa,name="criar_pessoa"),
]