from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_setor, name='lista_setor'),
    path('adicionar/', views.add_setor, name='add_setor'),
    path('editar/<int:id>/', views.editar_setor, name='editar_setor'),
    path('excluir/<int:id>/', views.excluir_setor, name='excluir_setor'),
]
