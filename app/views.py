from .models import Tarefas
from rest_framework.decorators import api_view
from .serializers import Tarefa_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound



class TarefasView(APIView):
    def get(self, request):
        tarefas = Tarefas.objects.all()
        serializer = Tarefa_serializer(tarefas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Tarefa_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Gerencia_Tarefas(APIView):
    def get_object(self, pk):
        try:
            return Tarefas.objects.get(pk=pk)
        except:
            raise NotFound()


    def get(self, request, pk):
        tarefas = self.get_object(pk)
        serializer = Tarefa_serializer(tarefas)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        tarefas = self.get_object(pk)
        serializer = Tarefa_serializer(tarefas, request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefas = self.get_object(pk)
        tarefas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        

"""@api_view(['GET', 'POST'])
def list_tarefas(request):
    if request.method == 'GET':
        tarefas = Tarefas.objects.all()
        serializer = Tarefa_serializer(tarefas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Tarefa_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


# O nome da função será o nome do título colocado na página de manipulação.

"""@api_view(['GET', 'PUT', 'DELETE'])
def gerenciar_tarefas(request, pk):
    try:
        tarefas = Tarefas.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Tarefa_serializer(tarefas)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = Tarefa_serializer(tarefas, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tarefas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
