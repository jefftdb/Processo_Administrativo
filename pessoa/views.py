from django.shortcuts import render
from pessoa.models import Pessoa

from django.http import HttpResponse

def minha_view(request):
    return HttpResponse("Olá do Django!")