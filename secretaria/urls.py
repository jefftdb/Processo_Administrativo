from django.urls import path
from secretaria.views import *

urlpatterns = [
    path('add_secretaria/', add_secretaria, name='add_secretaria'),
    path('secretarias/', lista_secretaria, name='lista_secretaria'),
    path('secretarias/excluir/<int:id>/', excluir_secretaria, name='excluir_secretaria'),
    path('secretarias/editar/<int:id>/', editar_secretaria, name='editar_secretaria'),
]