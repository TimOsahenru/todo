from django.urls import path
from app import views


urlpatterns = [
    path('create/', views.create_todo, name='create_todo'),
    path('', views.all_todos, name='todo_list'),
]
