import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import PessoaProcesso, Pessoa, Processo,Funcionario,Administrador
from django.contrib.auth.models import Group


def listar_pessoa_processos(request):
    dados = []
    for pp in PessoaProcesso.objects.select_related("pessoa", "processo"):
        dados.append({
            "id": pp.id,
            "codigo": pp.codigo,
            "pessoa": {
                "id": pp.pessoa.id,
                "username": pp.pessoa.username,
                "cpf": pp.pessoa.cpf,
            },
            "processo": {
                "id": pp.processo.id,
                "titulo": pp.processo.titulo,
            },
            "data": pp.data,
        })
    return JsonResponse(dados, safe=False)

def visualizar_pessoa_processo(request, id):
    pp = get_object_or_404(PessoaProcesso.objects.select_related("pessoa", "processo"), id=id)
    return JsonResponse({
        "id": pp.id,
        "codigo": pp.codigo,
        "pessoa": {
            "id": pp.pessoa.id,
            "username": pp.pessoa.username,
            "cpf": pp.pessoa.cpf,
        },
        "processo": {
            "id": pp.processo.id,
            "titulo": pp.processo.titulo,
        },
        "data": pp.data,
    })


@csrf_exempt
def criar_pessoa_processo(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body.decode("utf-8"))
            
            pessoa = get_object_or_404(Pessoa, id=dados.get("pessoa_id"))
            processo = get_object_or_404(Processo, id=dados.get("processo_id"))

            pp = PessoaProcesso.objects.create(
                codigo=PessoaProcesso.gerar_codigo_unico(),
                pessoa=pessoa,
                processo=processo,
                data=timezone.now()
            )

            return JsonResponse({"id": pp.id, "mensagem": "PessoaProcesso criado com sucesso"})
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)


@csrf_exempt
def editar_pessoa_processo(request, id):
    if request.method == "PUT":
        try:
            pp = get_object_or_404(PessoaProcesso, id=id)
            dados = json.loads(request.body.decode("utf-8"))

            if "codigo" in dados:
                pp.codigo = dados["codigo"]
            if "pessoa_id" in dados:
                pp.pessoa = get_object_or_404(Pessoa, id=dados["pessoa_id"])
            if "processo_id" in dados:
                pp.processo = get_object_or_404(Processo, id=dados["processo_id"])
            
            pp.save()
            return JsonResponse({"mensagem": "PessoaProcesso atualizado com sucesso"})
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)

@csrf_exempt
def excluir_pessoa_processo(request, id):
    if request.method == "DELETE":
        pp = get_object_or_404(PessoaProcesso, id=id)
        pp.delete()
        return JsonResponse({"mensagem": "PessoaProcesso excluído com sucesso"})
    
@csrf_exempt
def criar_pessoa(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body.decode("utf-8"))
            
            pessoa = Pessoa.objects.create_user(username=dados["username"], password=dados["password"],
                                                first_name=dados["first_name"],last_name=dados["last_name"],email=dados["email"],
                                                cpf=dados["cpf"],telefone=dados["telefone"],is_staff=True, is_superuser=True)
            grupo_pessoa = Group.objects.get(name='Pessoa')
            pessoa.groups.add(grupo_pessoa)
            
            
            return JsonResponse({"mensagem": "Usuário criado com sucesso!"})
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)
        
@csrf_exempt
def criar_funcionario(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body.decode("utf-8"))
            
            funcionario = Funcionario.objects.create_user(username=dados["username"], password=dados["password"],
                                                first_name=dados["first_name"],last_name=dados["last_name"],email=dados["email"],
                                                cpf=dados["cpf"],telefone=dados["telefone"],is_staff=True, is_superuser=True)
            grupo_pessoa = Group.objects.get(name='Funcionario')
            funcionario.groups.add(grupo_pessoa)
            
            
            return JsonResponse({"mensagem": "Funcionário criado com sucesso!"})
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)
        
@csrf_exempt
def criar_admin(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body.decode("utf-8"))
            
            administrador = Administrador.objects.create_user(username=dados["username"], password=dados["password"],
                                                first_name=dados["first_name"],last_name=dados["last_name"],email=dados["email"],
                                                cpf=dados["cpf"],telefone=dados["telefone"],is_staff=True, is_superuser=True)
            grupo_pessoa = Group.objects.get(name='Administrador')
            administrador.groups.add(grupo_pessoa)
            
            
            return JsonResponse({"mensagem": "Administrador criado com sucesso!"})
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)