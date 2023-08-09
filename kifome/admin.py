from django.contrib import admin

from kifome.models import Aluno, Turma, Cardapio


# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'nome']
    fields = ['cpf', 'nome']


class TurmaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'ano']
    fields = ['curso', 'ano']


class CardapioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
    fields = ['nome', 'descricao']


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Cardapio, CardapioAdmin)
