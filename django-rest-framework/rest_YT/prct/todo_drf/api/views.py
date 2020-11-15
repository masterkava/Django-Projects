from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.
# applying the rest decorator
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update/',
        'Delete':'/task-delete/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True) #this will serialize the task 
    return Response(serializer.data) #this will serialise the data and return it to the api response

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.all(id=pk)
    serializer = TaskSerializer(tasks, many=False) #this will serialize the task 
    return Response(serializer.data) #this will serialise the data and return it to the api response


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item deleted Successfully")

