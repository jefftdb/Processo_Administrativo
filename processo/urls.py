from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_processos, name='lista_processos'),
    path('adicionar/', views.adicionar_processo, name='adicionar_processo'),
    path('editar/<int:id>/', views.editar_processo, name='editar_processo'),
    path('excluir/<int:id>/', views.excluir_processo, name='excluir_processo'),
    path('<int:id>/', views.detalhe_processo, name='detalhe_processo'),
    
]