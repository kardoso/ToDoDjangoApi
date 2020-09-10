from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task/<str:id>/', views.taskDetail, name="task-detail"),
    path('create-task/', views.createTask, name="create-task"),
    path('update-task/<str:id>/', views.updateTask, name="update-task"),
    path('delete-task/<str:id>/', views.deleteTask, name="delete-task"),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', views.register, name='register'),
]