from django.contrib import admin
from .models import Filme, Episodio, Usuario  # Importa o arquivo models (dentro da mesma pasta), importar a classe criada
from django.contrib.auth.admin import UserAdmin  # Gerencia o usuario


# Modelo para criar novos campos personalizados, para ser acessado no administrativo do site, nos Usuarios
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", # descrição do campo criado
        {'fields': ( # Campos que serão criados
            'filmes_vistos',  # campo de filmes_vistos
            'episodios_vistos'  # campo de episodios_vistos
        )
        }
    )
)
UserAdmin.fieldsets = tuple(campos)  # Após alteração dos campos, retornar como uma tupla para o fieldset no Administrativo


# Register your models here.
admin.site.register(Filme)  # Tabela Filme registrada e visível no admin do site
admin.site.register(Episodio)  # Tabela Episodio registrada e visível no admin do site
admin.site.register(Usuario, UserAdmin)  # Importar Usuário













