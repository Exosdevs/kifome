from django.db import models


# Create your models here.


ok

ORD_ENTRADA = [
        ("A", "A - Primeiro Semestre"),
        ("B", "B - Segundo Semestre"),
    ]

class Turma(models.Model):
    curso = models.CharField(blank=False, null=False, max_length=100)
    ano = models.CharField(blank=False, null=False, max_length=4)
    ordem = models.CharField(blank=False, null=False, max_length=2, choices=ORD_ENTRADA)


class Aluno(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=256)
    cpf = models.CharField(blank=False, null=False, unique=True, max_length=14)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)


class Cardapio(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=120)
    descricao = models.TextField(blank=False, null=False)
    data = models.DateField(blank=False, null=False, unique=True)



class Turma(models.Model):
    curso = models.CharField(max_length=255)
    ano = models.CharField(max_length=4)
    ordem = models.CharField(max_length=1)

    def __str__(self):
        return self.curso


class Aluno(models.Model):
    cpf = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    restricao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    cnpj = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)


class Cardapio(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=30)
    data = models.DateField()


class Pedido(models.Model):
    pessoa = models.ManyToManyField(Aluno)
    restricao = models.BooleanField(default=False)
    data = models.DateField()
