from django import views
from django.urls import path
#from .views import list_tarefas, gerenciar_tarefas
from .views import TarefasView, Gerencia_Tarefas


urlpatterns = [
    #path('', list_tarefas),
    #path('<int:pk>', gerenciar_tarefas),
    path('', TarefasView.as_view()),
    path('<int:pk>', Gerencia_Tarefas.as_view())
]

