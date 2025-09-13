from django.urls import path
from processo import views

urlpatterns = [
    path('', views.vizualizarProcesso, name='vizualizarProcesso'),
    path('add/', views.add_processo, name='add_processo'),
]