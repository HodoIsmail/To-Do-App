from django.shortcuts import render, get_object_or_404
from django.views import generic
from . models import Task

# Create your views here.

# def index(request):
#     tasks = Task.objects.all()
#     context = {'tasks': tasks}
#     return render(request, 'index.html', context)
class TaskList(generic.ListView):
    queryset = Task.objects.all()
    template_name= "tasks/index.html"

def task_details(request):
    queryset = Task.objects.all()
    task= get_object_or_404(queryset)
    return render(request, 'tasks/index.html', {'task': task},)
