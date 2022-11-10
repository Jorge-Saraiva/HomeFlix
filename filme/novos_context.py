from .models import Filme

# Criando funções com todos os nossos filmes

# Criando uma função com os filmes recentes
def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]  # Ordena por data decrescente
    return {"lista_filmes_recentes": lista_filmes}


# Criando uma lista de filmes em alta
def lista_filmes_populares(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    lista_filmes_emalta = []
    for filme in lista_filmes:
        if filme.visualizacoes > 0:
            lista_filmes_emalta.append(filme)
    return {"lista_filmes_populares": lista_filmes_emalta}


# Função para escolhar o método para o filme destaque
def filme_destaque(request):
    filme = Filme.objects.order_by('-data_criacao')  # Escolha para o filme destaque
    if filme:
        filme = filme[0]
    else:
        None
    return {"filme_destaque": filme}

















