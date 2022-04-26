
from rest_framework import serializers
from .models import Tarefas


# Não esquecer da Meta
# Esta classe armazena metadados do model, a existencia desta classe serve simplesmente para separar os atributos do model de seus metadados. 
# É apenas uma questão de escopo/namespace e por isso não há necessidade de herdar.

class Tarefa_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefas
        fields = ['nome', 'done', 'created_at', 'updated']
        