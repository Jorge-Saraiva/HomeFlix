from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser  # Classe padrão django para criar usuários

# Create your models here.


# Criar uma lista de categorias, para passar para a classe 'Filme'
LISTA_CATEGORIAS = (
    ("ACAO", "Ação"),
    ("ANALISE", "Análise"),  # Passar 2 informações (1ª o que será armazenada no Banco de Dados e a 2ª que irá aparecer para o usuário)
    ("ANIME", "Anime"),
    ("APRESENTACAO", "Apresentação"),
    ("COMEDIA", "Comédia"),
    ("PROGRAMACAO", "Programação"),
    ("SUSPENSE", "Suspense"),
    ("OUTROS", "Outros"),
)

# Criar o Filme (estruturar a tabela dos filmes)
class Filme(models.Model):
    titulo = models.CharField(max_length=100)  # Definir o tipo do campo com um máximo de caracteres
    thumb = models.ImageField(upload_to='thumb_filmes')  # Campo de imagem do filme com parâmetro de um local para armazenar as imagens
    descricao = models.TextField(max_length=1000)  # Campo de texto em bloco
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)  # Categoria de uma lista de itens (2 parâmetros - max_length e choices='lista criada das categorias, acima da classe filme'
    visualizacoes = models.IntegerField(default=0)  # Quantidade de visualizações padrão quando criado um filme
    data_criacao = models.DateTimeField(default=timezone.now)  # Criação de um campo de data com hora com padrão de horário, caso o admin não informe a data (pega o horário do sistema do computador

    # Altera o formato do titulo que será mostrado no admin do site
    def __str__(self):
        return self.titulo

# Criar os episódios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)  # Chave estrangeira (passar tabela como string)
    # related_name = Permite acessar todos os episódios relacionados a um filme
    # on_delete=models.CASCADE = Excluí todos os arquivos relacionados a um filme
    titulo = models.CharField(max_length=100)
    #video = models.FileField(upload_to="media/videos")
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


# Criar o Usuário
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")  # Relação muitos para muitos (relacionamento entre itens e usuários)
    episodios_vistos = models.ManyToManyField("Episodio")




