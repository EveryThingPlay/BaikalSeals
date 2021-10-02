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
        if request.user.is_authenticated == True:
            for i in task.objects.all():
                if str(i.owner.email) == str(request.user.email):
                    Serializer = TaskSerializer(i)
                    return Response(Serializer.data)
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
    
    def put(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            task_object = task.objects.get()
            data = request.data
            task_object.todo = data["todo"]
            task_object.owner = data["owner"]
            task_object.proof = data["proof"]
            task_object.target = data["target"]


        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)




