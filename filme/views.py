from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin  # Classe a ser passada para a Class Base Views, para o django gerenciar as páginas que queremos bloquear


# LoginRequireMixin deve ser passada como 1º parâmetro


# TEMOS 2 FORMAS DE CONSTRUIR UMA VIEW
"""
Function Base Views
    - Cria uma função para cada view
    - Mais simples/prática 
    - Admin quem precisa criar as views
    - Projetos menores
    
Class Base Views
    - O Django entrega muitas configurações prontas
    - Projetos maiores
"""


# Create your views here.

# FUNCTION BASE VIEWS
def homepage(request):
    # request = Requisição (GET-> Pegando informações do site - ou POST -> preenche um formulário para um site)
    return render(request, "homepage.html")  #Necessário passar 2 parâmetros para o 'render' (request e a página html)


# Para pegar filmes do banco de dados e trazer para a página, é necessário passsar um 'context', que é um dicionário, que será passado como um parâmetro, que irá permitir usar tags python no HTML

# Obs. O 'render' permite passar um 3º parâmetro (context)

# FUNCTION BASE VIEWS
def homefilmes(request):
    context = {}
    lista_filmes = Filme.objects.all()  # pega todos os filme do banco de dados
    context['lista_filmes'] = lista_filmes
    return render(request, "homefilmes.html", context)


# ------------------------------------------------------------

# DEFININDO CLASS BASE VIEWS

class Homepage(FormView):  # FormView necessita de um ' template_name ' e um ' form_class '
    template_name = "homepage.html"  # Obrigatório usar o template_name com o TemplateView
    form_class = FormHomepage

    # Redirecionando usuário caso autenticado
    def get(self, request, *args, **kwargs):
        # Verificando se usuário está autenticado
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criar_conta')


class Homefilmes(LoginRequiredMixin, ListView):  # ListView exibe uma lista de objetos do banco de dados
    # Obrigatório usar o template_name e o modelo com o ListView
    template_name = "homefilmes.html"
    model = Filme
    # Essa classe passa as informações como 'object_list', que é a mesma coisa que o 'lista_filmes' (lista de itens do nosso modelo)


class Detalhesfilme(LoginRequiredMixin, DetailView):  # DetailView exige que seja passado uma forma de identificar qual filme está sendo acessado (Ex. <pk>)
    template_name = "detalhesfilme.html"  # Template será replicado de acordo com os diferentes filmes
    model = Filme
    # object -> 1 item do nosso modelo


    # Definir uma funçaõ get, referente o metodo de requisição
    def get(self, request, *args, **kwargs):
        # descobrir o filme acessado
        filme = self.get_object()
        # Somar 1 nas visualizações
        filme.visualizacoes += 1
        # Quando editar um campo no banco de dados, deverá salvar esse filme, para a alteração ser registrada no banco de dados
        filme.save()
        # Configuração, para adicionar campo "Continuar Assistindo"
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super(Detalhesfilme, self).get(request, *args, **kwargs)  # Redireciona o usuário para a url final


    # Passar uma variável para uma view especifica
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)  # Classes herdam parâmetros da 'super'
        # filtrando a tabela de filmes pegando os filmes que têm as mesmas categorias
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:9]  # Define a quantidade de filmes relacionados que serão mostrados
        context["filmes_relacionados"] = filmes_relacionados
        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def queryset(self):
        termo_pesquisa = self.request.GET.get("query")
        termo_pesquisa = termo_pesquisa.strip()
        termo_pesquisa = termo_pesquisa.upper()
        termo_pesquisa = termo_pesquisa.replace('Ç', 'C').replace('Ã', 'A').replace('Õ', 'O').replace('Á', 'A').replace('É', 'E').replace('Ê', 'E').replace('Â', 'A').replace('Ô', 'O').replace('Í', 'I').replace('Ú', 'U')
        # Verificando se o usuário efetuou a pesquisa
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)  # '__icontains' significa se contém algo em um object_list
            if len(object_list) == 0:
                object_list = self.model.objects.filter(categoria__icontains=termo_pesquisa)  # '__icontains' significa se contém algo em um object_list
            return object_list
        else:
            object_list = self.model.objects.all()
            return object_list


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editar_perfil.html'
    model = Usuario  # Informar a tabela que o usuário irá editar
    fields = ['first_name', 'last_name', 'email']  # informar os campos que terá para o usuário editar

    def get_success_url(self):
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    template_name = 'criar_conta.html'
    form_class = CriarContaForm  # Formulário que cria um item no banco de dados

    # Função que verifica se todos os campos do formulário foram preenchidos
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # Sempre que criar um ' FormView ' deverá criar um get_success_url
    def get_success_url(self):
        # Deverá retornar um link
        return reverse('filme:login')






