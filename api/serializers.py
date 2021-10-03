from rest_framework import serializers
from .models import position, CustomUser, task

class UserSerializer(serializers.ModelSerializer):
    """Полные данные о пользователе"""
    class Meta:
        model = CustomUser
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    """Список должностей"""
    class Meta:
        model = position
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    """Обработка регистрации пользователей"""
    
    password2 = serializers.CharField(style={'input-type': 'password'}, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ("email", "password", "password2", "role", "first_name", "last_name", "is_active")
        extra_kwargs = {'password': {'write_only':True}}

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password' : 'passwords must match'})

        user = CustomUser(
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            is_active = False,
            role = self.validated_data['role'],
        )
        user.set_password(password)
        user.save()
        return user

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'
    def save(self):
        email = self.validated_data['owner']
        for i in CustomUser.objects.all():
            if i.email == email:
                newowner = i
        newtask = task(
            target = self.validated_data['target'],
            todo = self.validated_data['todo'],
            proof = self.validated_data['proof'],
            owner = newowner
        )
        return newtask