from django.shortcuts import render,redirect

# Create your views here.

from .models import Tarefa
from django.http import HttpResponse

def listar_tarefas(request):
    #1 a busca no banco de dados continua a mesma
    tarefas_salvas = Tarefa.objects.all()
    #2 criamos um  dicionario de contexto para enviar os dados ao template
    #a chave 'minhas_tarefas',será a variavel que usamos no html 
    contexto = {
        'minhas_tarefas': tarefas_salvas
    }

from django.shortcuts import render, get_object_or_404
from .models import Tarefa

def listar_tarefas(request):
    # 1. a busca no banco de dados continua a mesma
    tarefas_salvas = Tarefa.objects.all()

    # 2. criamos um "dicionario do contexto" para enviar os dados ao template.
    # A chave 'minhas_tarefas' será a variável que usaremos no html.
    contexto = {
        'minhas_tarefas': tarefas_salvas 
    }

    # 3. renderizamos o tamplate, passando a requisição e o contexto com os dados.
    return render(request, 'tarefas/lista.html', contexto)

def detalhe_tarefa (request, tarefa_id):
    #Busca uma tarefa pelo id
    #Se não encontrar retorna um erro 404
    tarefa= get_object_or_404 (Tarefa, pk=tarefa_id)

    return render(request, 'tarefas/detalhe.html', {'tarefa':tarefa})



#3. renderizamos o template , passando a requesição e o contexto com os dados. 
    return render(request, 'tarefas/lista.html', contexto)

def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(titulo=titulo,descricao=descricao)
        return redirect('lista_tarefas')

    return render(request,'tarefas/form_tarefa.html')

#me fodos http
#POST: envia dados para o servidor
#GET: busca dados no servidor 
#PUT: atualizada recursos existentes
#DELETES: remove recursos selecionados


def alterar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get('projeto')
        concluida = request.POST.get('concluido') == 'on' 

      
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.concluido = concluida
        
        tarefa.save()
        
        return redirect('lista_tarefas')

    context = {
        'tarefa': tarefa,
    }
    return render(request, 'tarefas/form_tarefa.html', context)

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk = tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render (request,'tarefas/confirmar_exclusao.html',{'tarefa':tarefa})