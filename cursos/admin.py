from django.contrib import admin
from cursos.models import Curso #importação do modelo

# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo','nivel','carga_horaria','data_do_curso'] #quais campos exibir
    search_fields = ['titulo','nivel'] #quais campos pesquisar
    list_filter = ['data_do_curso'] #filtros
