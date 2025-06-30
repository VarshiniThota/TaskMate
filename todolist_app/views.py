from django.shortcuts import get_object_or_404, render, redirect
from todolist_app.models import Tasklist
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST['task']
        deadline = request.POST['deadline']
        Tasklist.objects.create(tasks=task, deadline=deadline, manage=request.user)
        messages.success(request, "New task added!!")
        return redirect('home')
    else:
        all_task = Tasklist.objects.filter(manage=request.user).order_by('done','deadline')
        pg = Paginator(all_task, 3)
        page = request.GET.get('page')
        two_task = pg.get_page(page)
        context = {'all_task': all_task, 'two_task': two_task}
        return render(request, 'home.html', context)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tasklist, id=task_id)
    if task.manage == request.user:
        task.delete()
        messages.success(request, "Task deleted successfully!")
    else:
        messages.error(request, "You cannot access this page!")
    return redirect('home')


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Tasklist, id=task_id)
    if task.manage != request.user:
        messages.error(request, "You cannot access this page!")
        return redirect('home')

    if request.method == 'POST':
        task.tasks = request.POST.get("task")
        task.deadline = request.POST.get("deadline") or None
        task.done = 'done' in request.POST
        task.save()
        messages.success(request, "Task edited successfully!")
        return redirect('home')

    context = {'task': task}
    return render(request, 'edit.html', context)


@login_required
def status_edit(request, task_id):
    task = get_object_or_404(Tasklist, id=task_id)
    if task.manage == request.user:
        task.done = not task.done
        task.save()
    else:
        messages.error(request, "You cannot access this page!")
    return redirect('home')


def landing_page(request):
    return render(request, 'landing_page.html')
