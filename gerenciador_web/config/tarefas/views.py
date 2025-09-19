from django.shortcuts import render
from .models import Tarefa
#from django.http import HttpResponse

# Create your views here.

# def listar_tarefas(request):

#     tarefas_salvas = Tarefa.objects.all()
#     print(tarefas_salvas)
#     return HttpResponse("View 'listar_tarefas' executada! Confira no terminal")

def listar_tarefas(request):
    # 1. A busca no banco de dados continua a mesma
    tarefas_salvas = Tarefa.objects.all()

    # 2. Criamos um "dicionario de contexto para enviar os dados ao template"
    # A chave 'minhas_tarefas' será a variavel que usaram HTML.
    contexto = {
        'minhas_tarefas': tarefas_salvas
    }

    # 3. renderizamos o template, passando a requisição e o contexto com os dados.
    return render(request, 'tarefas/lista.html', contexto)