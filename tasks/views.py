from django.shortcuts import render, get_object_or_404
from django.views import generic
from . models import Task
from .forms import TaskForm

# Create your views here.

# def index(request):
#     tasks = Task.objects.all()
#     context = {'tasks': tasks}
#     return render(request, 'index.html', context)
# class TaskList(generic.ListView):
#     queryset = Task.objects.all()
#     template_name= "tasks/index.html"

def task_details(request):
    tasks = Task.objects.all()
    
    task_form = TaskForm()
    
    return render(request, 
    'tasks/index.html',
     {'tasks': tasks},
     {'task_form': task_form})
