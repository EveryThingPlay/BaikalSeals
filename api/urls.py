from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('positions', views.positionListView.as_view()),
    path('user', views.UserView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('tasks/', views.TaskListView.as_view()),
    path('tasks/<int:n>', views.ModifyTaskView.as_view()),
]