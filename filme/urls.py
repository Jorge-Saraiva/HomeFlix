# CRIANDO AS PÁGINAS DO SITE

# PARA CRIAR UMA PÁGINA DE UM SITE, É NECESSÁRIO SEGUIR 3 PASSOS

# 1º - CRIAR UMA URL
# 2º - CRIAR UMA VIEW (CÓDIGO EM PYTHON QUE IRÁ DIZER O QUE IRÁ ACONTECER QUANDO ACESSAR UM LINK)
# 3º TEMPLATE - PARTE VISUAL DO SITE (HTML)

from django.urls import path, include, reverse_lazy
from .views import homepage, homefilmes, Homepage, Homefilmes, Detalhesfilme, Pesquisafilme, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view

# Configurando templates utilizando o FUNCTION BASE VIEWS
"""
urlpatterns = [
    path('', homepage),  # Configurando a página padrão do site
    path('filmes/', homefilmes),
]
"""

# Configurando templates utilizando o CLASS BASE VIEWS

app_name='filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),  # Gerencia a requisição do usuário
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editar_perfil/<int:pk>', Paginaperfil.as_view(), name='editar_perfil'),
    path('criar_conta/', Criarconta.as_view(), name='criar_conta'),
    path('mudar_senha/', auth_view.PasswordChangeView.as_view(template_name='editar_perfil.html', success_url=reverse_lazy('filme:homefilmes')), name='mudar_senha'),
]

# LoginView já passa para o HTML uma variável que se chama ' form '

















