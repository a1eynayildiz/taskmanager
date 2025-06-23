from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Task, Profile
from django.contrib.auth.models import User


from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    profile = request.user.profile

    if profile.role == 'superadmin':
        tasks = Task.objects.all()

    elif profile.role == 'admin':
        # Kendi atadığı user görevleri + kendisine atanan görevler
        tasks = Task.objects.filter(
            assigned_by=request.user,
            assigned_to__profile__role='user'
        ) | Task.objects.filter(
            assigned_to=request.user
        )

    elif profile.role == 'supervisor':
        tasks = Task.objects.filter(
            assigned_to=request.user
        ) | Task.objects.filter(assigned_by=request.user)

    else:
        tasks = Task.objects.filter(assigned_to=request.user)

    return render(request, 'core/task_list.html', {'tasks': tasks})




@login_required
def task_create(request):
    profile = request.user.profile

    if profile.role == 'superadmin':
        # Superadmin tüm kullanıcıları görebilir
        users = User.objects.exclude(id=request.user.id)
    elif profile.role == 'admin':
        # Admin sadece 'user' rolündekileri görebilir
        users = User.objects.filter(profile__role='user')
    else:
        return HttpResponseForbidden("Yetkiniz yok")

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        assigned_to_id = request.POST.get('assigned_to')

        if not (title and description and assigned_to_id):
            return render(request, 'core/task_create.html', {'users': users, 'error': 'Tüm alanları doldurun.'})

        assigned_to = get_object_or_404(User, id=assigned_to_id)

        Task.objects.create(
            title=title,
            description=description,
            assigned_to=assigned_to,
            assigned_by=request.user,
        )
        return redirect('task_list')

    return render(request, 'core/task_create.html', {'users': users})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    profile = request.user.profile

    if profile.role in ['admin', 'superadmin'] or \
       (profile.role == 'supervisor' and task.assigned_to.profile.role == 'user') or \
       task.assigned_to == request.user:
        pass
    else:
        return redirect('task_list')

    if request.method == 'POST':
        completed = request.POST.get('completed') == 'on'
        task.completed = completed
        task.save()
        return redirect('task_detail', pk=task.pk)

    return render(request, 'core/task_detail.html', {'task': task})
