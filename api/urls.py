from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task/<str:id>/', views.taskDetail, name="task-detail"),
    path('create-task/', views.createTask, name="create-task"),

]