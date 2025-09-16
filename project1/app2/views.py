from django.shortcuts import render
from rest_framework.generics import CreateAPIView , ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User 
from .models import Task
from .serializers import RegisterSerializer , TaskSerializer
from rest_framework.permissions import IsAuthenticated
 

# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class TaskListCreateView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    
