from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def taskList(request):
    taskList = Task.objects.all()
    tasks = TaskSerializer(taskList, many=True)
    return Response(tasks.data)

@api_view(['POST'])
def createTask(request):
    newTask = TaskSerializer(data=request.data)
    if newTask.is_valid():
        newTask.save()
    return Response(newTask.data)

@api_view(['POST'])
def editTask(request, pk):
    task = Task.objects.get(id=pk)
    editedTask = TaskSerializer(instance=task, data=request.data)
    if editedTask.is_valid():
        editedTask.save()
    return Response(editedTask.data)



@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response()