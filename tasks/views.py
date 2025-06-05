from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from rest_framework.decorators import action
from .serializers import TaskSerializer
from rest_framework.response import Response

# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    @action(detail=False, methods=['get'],  url_path='completed')
    def completed(self,request):
        task = Task.objects.filter(completed=True)
        serializer = self.get_serializer(task, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'] ,  url_path='pending')
    def completed(self,request):
        task = Task.objects.filter(completed=False)
        serializer = self.get_serializer(task, many=True)
        return Response(serializer.data)
    