from django.shortcuts import render
from .models import Tarefa
from django.http import HttpResponse

# Create your views here.

def listar_tarefas(request):
    tarefas_salvas = Tarefa.objects.all()
    print(tarefas_salvas)
    return HttpResponse("View 'listar_tarefas' executada! Confira no terminal")