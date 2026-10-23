"""
URL configuration for ListagemdeTarefas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from listadetarefas.views import TarefaCompleteView, TarefaCreateView, TarefaDeleteView, TarefaListView, TarefaUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TarefaListView.as_view(), name = "tarefa_list"),
    path("create", TarefaCreateView.as_view()),
    path("update/<int:pk>", TarefaUpdateView.as_view(), name = "tarefa_update"),
    path("delete/<int:pk>", TarefaDeleteView.as_view(), name = "tarefa_delete"),
    path("complete/<int:pk>", TarefaCompleteView.as_view()), name = "tarefa_complete")
]
