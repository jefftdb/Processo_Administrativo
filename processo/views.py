import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Processo
from datetime import datetime as time
from pessoa.models import PessoaProcesso,Pessoa

def listar_processos(request):
    processos = Processo.objects.all().values()
    return JsonResponse(list(processos), safe=False)


def visualizar_processo(request, id):
    processo = get_object_or_404(Processo, id=id)
    #pp = PessoaProcesso.objects.first(processo = processo)
    return JsonResponse({
        "id": processo.id,
        "titulo": processo.titulo,
        "descricao": processo.descricao,
        "data_criacao": processo.data_criacao,
        "data_edicao": processo.data_edicao,
        #"Código": pp.codigo,
    })


@csrf_exempt
def criar_processo(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body.decode("utf-8"))
            processo = Processo.objects.create(
                titulo=dados.get("titulo"),
                descricao=dados.get("descricao"),
                data_criacao=time.now()
            )
            return JsonResponse({"id": processo.id, "mensagem": "Processo criado com sucesso"})
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)


@csrf_exempt
def editar_processo(request, id):
    if request.method == "PUT":
        try:
            processo = get_object_or_404(Processo, id=id)
            dados = json.loads(request.body.decode("utf-8"))
            
            processo.titulo = dados.get("titulo", processo.titulo)
            processo.descricao = dados.get("descricao", processo.descricao)
            processo.data_edicao = time.now()
            processo.save()

            return JsonResponse({"mensagem": "Processo atualizado com sucesso"})
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)


@csrf_exempt
def excluir_processo(request, id):
    if request.method == "DELETE":
        processo = get_object_or_404(Processo, id=id)
        processo.delete()
        return JsonResponse({"mensagem": "Processo excluído com sucesso"})
