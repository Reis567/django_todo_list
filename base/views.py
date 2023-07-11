from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView
# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'