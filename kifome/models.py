from django.db import models


# Create your models here.




class Turma(models.Model):
    ORD_ENTRADA = [
        ("A", "A - Primeiro Semestre"),
        ("B", "B - Segundo Semestre"),
    ]
    curso = models.CharField(blank=False, null=False, max_length=255)
    ano = models.CharField(blank=False, null=False, max_length=4)
    ordem = models.CharField(blank=False, null=False, max_length=1, choices=ORD_ENTRADA)
    def __str__(self):
        return self.curso


class Aluno(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=255)
    cpf = models.CharField(blank=False, null=False, unique=True, max_length=14)
    senha = models.CharField(max_length=255)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    restricao = models.BooleanField(default=False)
    def __str__(self):
        return self.nome


class Cardapio(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=120)
    descricao = models.TextField(blank=False, null=False)
    data = models.DateField(blank=False, null=False, unique=True)
    def __str__(self):
        return self.nome


class Empresa(models.Model):
    cnpj = models.CharField(max_length=18)
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)


class Pedido(models.Model):
    pessoa = models.ManyToManyField(Aluno)
    pedido = models.ManyToManyField(Cardapio)
    restricao = models.BooleanField(default=False)
    data = models.DateField()
