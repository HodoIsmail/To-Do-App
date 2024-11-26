from django.shortcuts import render
from django.views import generic
from . models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)
# class TaskList(generic.ListView):
#     model = Task
