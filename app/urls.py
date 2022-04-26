from django import views
from django.urls import path
from .views import list_tarefas, gerenciar_tarefas


urlpatterns = [
    path('', list_tarefas),
    path('<int:pk>', gerenciar_tarefas)
]

