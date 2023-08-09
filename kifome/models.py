from django.db import models


# Create your models here.
class Turma(models.Model):
    curso = models.CharField(blank=False, null=False, max_length=100)
    ano = models.CharField(blank=False, null=False, max_length=4)
    ordem = models.CharField(blank=False, null=False, max_length=2)


class Aluno(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=256)
    cpf = models.CharField(blank=False, null=False, max_length=14)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)


class Cardapio(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=120)
    descricao = models.TextField(blank=False, null=False)
    data = models.DateField(blank=False, null=False)
