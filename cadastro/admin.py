from django.contrib import admin
from .models import Aluno, Professor, Sala, Aula, Matricula

admin.site.site_header = "Administração do Sistema de Cadastros"         # Título do cabeçalho do site admin
admin.site.site_title = "Administração de Cadastros"                     # Título do site admin
admin.site.register(Aluno)                                               # Registro do modelo Aluno no site admin
admin.site.register(Professor)
admin.site.register(Sala)
admin.site.register(Aula)                                              # Registro do modelo Curso no site admin
admin.site.register(Matricula)