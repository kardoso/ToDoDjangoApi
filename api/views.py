from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Task list': '/task-list/',
        'Task details': '/task/<str:id>/',
        'Create task': '/create-task/',
        'Edit task': '/update-task/<str:id>/',
        'Delete task': '/delete-task/<str:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)