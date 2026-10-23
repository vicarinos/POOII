from datetime import date

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View

from listadetarefas.models import tarefa

# Create your views here.

class TarefaListView(ListView):
    model = tarefa

class TarefaCreateView (CreateView):
    model = tarefa
    fields = ["titulo", "prazoLimite", 
              "terminado_em", "pessoa_responsavel"]
    success_url = reverse_lazy("tarefa_list")

class TarefaUpdateView (UpdateView):
    model = tarefa
    fields = ["titulo", "prazoLimite", 
                  "pessoa_responsavel"]
    success_url = reverse_lazy("tarefa_list")

class TarefaDeleteView (DeleteView):
    model = tarefa
    success_url = reverse_lazy("tarefa_list")

class TarefaCompleteView(View):
    def get(self, request, pk):
        tarefa = get_object_or_404(tarefa, pk=pk)
        tarefa.terminado_em = date.today()
        tarefa.save()
        return redirect("tarefa_list")