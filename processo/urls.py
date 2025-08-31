from django.urls import path
from processo import views

urlpatterns = [
    path('', views.vizualizarProcesso, name='vizualizarProcesso'),
]