from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils import timezone
from .models import task, taskForm

# Create your views here.


def index(request):
    latest_task = task.objects.all()
    context = {'latest_task': latest_task}
    return render(request, 'tasks/index.html', context)


def new(request):
    return render(request, 'tasks/new.html')


def create(request):
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            task_data = form.save(commit=False)
            task_data.timestamp = timezone.now()
            task_data.save()
            form.save_m2m()
            messages.success(request, 'Task created')
            return HttpResponseRedirect(reverse('tasks:index'))
        messages.error(request, form.errors)
        return render(request, 'tasks/new.html', {'form': form})


def show(request, task_id):
    show_task = get_object_or_404(task, pk=task_id)
    return render(request, 'tasks/show.html', {'task': show_task})


def edit(request, task_id):
    edit_task = get_object_or_404(task, pk=task_id)
    return render(request, 'tasks/new.html', {'task': edit_task})


def update(request, task_id):
    update_task = get_object_or_404(task, pk=task_id)
    try:
        selected_name = task.objects.get(pk=request.POST['name'])
    except (KeyError, task.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'tasks/edit.html', {
            'task': task,
            'error_message': "You didn't select a Task",
        })
    else:
        update_task.name = selected_name
        update_task.save()
        messages.success(request, 'Task updated')
        return HttpResponseRedirect(reverse('tasks:show', args=(task.id,)))


def delete(request, task_id):
    delete_task = get_object_or_404(task, pk=task_id)
    delete_task.delete()
    messages.error(request, 'Task Deleted')
    return HttpResponseRedirect(reverse('tasks:index'))
