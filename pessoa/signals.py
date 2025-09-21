from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from processo.models import Processo

@receiver(post_migrate)
def criar_grupos_padrao(sender, **kwargs):
    if sender.name == "pessoa":  # evita rodar em todos os apps
        grupo_pessoa, _ = Group.objects.get_or_create(name='Pessoa')
        grupo_funcionario, _ = Group.objects.get_or_create(name='Funcionario')
        grupo_admin, _ = Group.objects.get_or_create(name='Administrador')

        # Atribuir permissões aos grupos
        ct = ContentType.objects.get_for_model(Processo)
        permissoes = Permission.objects.filter(content_type=ct)

        grupo_pessoa.permissions.set(permissoes.filter(codename__startswith='view'))
        grupo_funcionario.permissions.set(permissoes.exclude(codename__startswith='view'))
        grupo_admin.permissions.set(permissoes)
