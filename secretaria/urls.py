from django.urls import path
from secretaria import views

urlpatterns = [
    path('', views.vizualizarSecretaria, name='vizualizarSecretaria'),
]