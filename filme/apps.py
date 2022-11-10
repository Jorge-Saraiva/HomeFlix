from django.apps import AppConfig


# Ao incluir o nome do app no Settings, cria automaticamente essa classe, com o nome do nosso app
class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'
