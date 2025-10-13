from django.db import models
from pessoa.models import Pessoa
import random, string
from datetime import date

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
        while True:
            letras = ''.join(random.choices(string.ascii_uppercase, k=3))
            numeros = ''.join(random.choices(string.digits, k=3))
            codigo = letras + numeros
            if not PessoaProcesso.objects.filter(codigo=codigo).exists():
                return codigo

    def __str__(self):
        return f"{self.processo} -> {self.pessoa} ({self.data_inicio})"



Processo.pessoas = models.ManyToManyField(
    Pessoa,
    through=PessoaProcesso,
    related_name="processos"
)
