from django.contrib.auth.models import AnonymousUser
from django.http import response
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import position, CustomUser, task
from rest_framework.response import Response
from .serializers import PositionSerializer, RegisterSerializer, TaskSerializer, UserSerializer


class positionListView(APIView):
    """Список должностей"""
    def get(self, request):
        if request.user.is_authenticated == True:
            positions = position.objects.all()
            serializer = PositionSerializer(positions, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserView(APIView):
    """Вывод данных о пользвателе"""
    def get(self, request):
        if str(request.user) != 'AnonymousUser':
            for i in CustomUser.objects.all():
                if str(i.email) == str(request.user.email):
                    serializer = UserSerializer(i)
                    return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class TaskListView(APIView):
    def get(self, request):
        tasks = []
        data = {}
        if request.user.is_authenticated == True:
            user = request.user
            tasks = task.objects.filter(owner=user)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
            
    def post(self, request):
        if request.user.is_authenticated == True:
            serializer = TaskSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                newtask = serializer.save()
                data["target"] = newtask.target
                data["todo"] = newtask.todo
                data["proof"] = newtask.proof
                data["owner"] = newtask.owner
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors)
    
class ModifyTaskView(APIView):
    def put(self, request, n, *args, **kwargs,):
        if request.user.is_authenticated == True:
            task_object = task.objects.get(id=n)
            data = request.data
            email = data["owner"]
            for i in CustomUser.objects.all():
                if email == i.email:
                    newowner = i
            task_object.todo = data["todo"]
            task_object.owner = newowner
            task_object.proof = data["proof"]
            task_object.target = data["target"]
            task_object.save()
            serializer = TaskSerializer(task_object)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
