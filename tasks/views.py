from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')

        Task.objects.create(
            title=title,
            description=description,
            deadline=deadline,
            status=status,
            user=request.user
        )
        return redirect('/')

    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('/')


@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id, user=request.user)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.deadline = request.POST.get('deadline')
        task.status = request.POST.get('status')
        task.save()
        return redirect('/')

    return render(request, 'edit.html', {'task': task})