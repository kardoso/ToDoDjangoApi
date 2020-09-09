from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .serializers import TaskSerializer, UserSerializer
from .models import Task

from django.contrib.auth.models import User 
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Task list': '/task-list/',
        'Task details': '/task/<str:id>/',
        'Create task': '/create-task/',
        'Edit task': '/update-task/<str:id>/',
        'Delete task': '/delete-task/<str:id>/',
        'Receive authentication token': '/token-auth/'
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def taskList(request, format=None):
    tasks = Task.objects.filter(author=request.user.username)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def taskDetail(request, id):
    task = Task.objects.get(id=id)
    if task.author != request.user.username:
        raise PermissionDenied({"message":"You don't have permission to do this"})
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def createTask(request):
    request.data.update({"author": request.user.username})
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def updateTask(request, id):
    task = Task.objects.get(id=id)
    if task.author != request.user.username:
        raise PermissionDenied({"message":"You don't have permission to do this"})
    serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteTask(request, id):
    task = Task.objects.get(id=id)
    if task.author != request.user.username:
        raise PermissionDenied({"message":"You don't have permission to do this"})
    task.delete()
    return Response("Task deleted")