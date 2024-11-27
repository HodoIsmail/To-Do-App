from django.shortcuts import render, redirect
from django.views import generic
from .models import Task
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

    if request.method == 'POST':
        
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
        

    form = TaskForm()

    return render(request, 
        'tasks/index.html',
        {'tasks': tasks,
         'task_form': form})
