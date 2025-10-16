from django.shortcuts import render
from .models import Projeto 
from django.http import HttpResponse 

# Create your views here.

def listar_projetos(request):
    """
    Lista todos os projetos salvos no banco de dados.
    """
    # 1. Busca todos os objetos Projeto
    projetos_salvos = Projeto.objects.all()

    # 2. Cria o dicionário de contexto para enviar os dados ao template.
    # A chave 'meus_projetos' será a variável que usaremos no html.
    contexto = {
        'meus_projetos': projetos_salvos
    }

    # 3. Renderiza o template, passando a requisição e o contexto com os dados.
    return render(request, 'projetos/lista.html', contexto) # Alterado o nome do template e a variável de contexto
