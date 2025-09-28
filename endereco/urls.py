from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_endereco, name='lista_endereco'),
    path('adicionar/', views.add_endereco, name='add_endereco'),
    path('editar/<int:id>/', views.editar_endereco, name='editar_endereco'),
    path('excluir/<int:id>/', views.excluir_endereco, name='excluir_endereco'),
]
