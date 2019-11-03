from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('todo', views.todo, name="todo"),
    path('time', views.show_time, name="show_time"),
    path('todo_item/<int:todo_id>', views.todo_item, name="todo_item")
]