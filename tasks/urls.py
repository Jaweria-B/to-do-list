from django.urls import path
from . import views

app_name = "todolist"

urlpatterns = [
    path("", views.index, name="index"),
    path("addtask/", views.add, name="addTask")
]