from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task/<str:id>/', views.taskDetail, name="task-detail"),
    path('create-task/', views.createTask, name="create-task"),
    path('update-task/<str:id>/', views.updateTask, name="update-task"),
    path('delete-task/<str:id>/', views.deleteTask, name="delete-task"),
]