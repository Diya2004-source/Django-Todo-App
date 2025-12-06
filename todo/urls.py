from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.todo_list, name='todo_list'),
]
