from django.db import models
from pessoa.models import Pessoa
import random, string
from datetime import datetime, date
from django.db.models import IntegerField
from django.db.models.functions import Cast, Substr

class Processo(models.Model):   
    titulo = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    data_edicao = models.DateField(null=True, blank=True)
    descricao = models.TextField()

    def save(self, *args, **kwargs):
        if self.pk:  # se já existe, é edição
            self.data_edicao = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class PessoaProcesso(models.Model):
    codigo = models.CharField(max_length=6)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    data_inicio = models.DateField(auto_now_add=True)
    data_termino = models.DateField(null=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = self.gerar_codigo_unico()
        super().save(*args, **kwargs)

    def gerar_codigo_unico(self):


        ano_atual = datetime.now().year

        processos_ano = PessoaProcesso.objects.filter(
            codigo__endswith=f"/{ano_atual}"
        )

        ultimo_processo = processos_ano.annotate(
            numero_int=Cast(Substr("codigo", 1, 5), IntegerField())
        ).order_by("numero_int").last()

        if ultimo_processo:
            numero = ultimo_processo.numero_int + 1
        else:
            numero = 1

        return f"{numero}/{ano_atual}"



Processo.pessoas = models.ManyToManyField(
    Pessoa,
    through=PessoaProcesso,
    related_name="processos"
)
