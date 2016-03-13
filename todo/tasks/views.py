from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import task

def index(request):
    latest_task = task.objects.all()
    context = {'latest_task': latest_task}
    return render(request, 'todoapp/index.html', context)

def show(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todoapp/show.html', {'question': question})

def edit(request, task_id):
    response = "You're looking at the task edit %s."
    return HttpResponse(response % task_id)