from django.http import HttpResponse
from django.shortcuts import render

from listadetarefas.models import tarefa

# Create your views here.

def home(request):
    return render(request, "listadetarefas/home.html")

def tarefa_listar(request):
    tarefas = tarefa.objects.all()
    return render(request, "listadetarefas/tarefa_listar.html", {"tarefas" : tarefas})
