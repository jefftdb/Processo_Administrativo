from django.urls import path
from processo import views

urlpatterns = [
    path("", views.listar_processos, name="listar_processos"),
    path("<int:id>", views.visualizar_processo, name="visualizar_processo"),
    path("criar/", views.criar_processo, name="criar_processo"),
    path("<int:id>/editar/", views.editar_processo, name="editar_processo"),
    path("<int:id>/excluir/", views.excluir_processo, name="excluir_processo"),
]