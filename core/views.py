from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
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
    if profile.role == 'admin':
        tasks = Task.objects.all()
    elif profile.role == 'supervisor':
        tasks = Task.objects.filter(assigned_to__profile__role='user') | Task.objects.filter(assigned_by=request.user)
    else:
        tasks = Task.objects.filter(assigned_to=request.user) | Task.objects.filter(assigned_by=request.user)
    return render(request, 'core/task_list.html', {'tasks': tasks})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from .models import Task

@login_required
def task_create(request):
    profile = request.user.profile

    # Sadece superadmin izinli
    if profile.role != 'superadmin':
        return HttpResponseForbidden("Bu işlemi yapmak için yetkiniz yok.")

    users = User.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        assigned_to_id = request.POST.get('assigned_to')

        if not title or not description or not assigned_to_id:
            error = "Lütfen tüm alanları doldurun."
            return render(request, 'core/task_create.html', {'users': users, 'error': error})

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

    # Sadece admin, supervisor veya görevin sahibi görebilir
    profile = request.user.profile
    if profile.role == 'admin' or \
       (profile.role == 'supervisor' and task.assigned_to.profile.role == 'user') or \
       (task.assigned_to == request.user):
        pass
    else:
        return redirect('task_list')  # Yetkisiz erişim engellenir

    if request.method == 'POST':
        # Görev tamamlandı işaretleme
        completed = request.POST.get('completed') == 'on'
        task.completed = completed
        task.save()
        return redirect('task_detail', pk=task.pk)

    return render(request, 'core/task_detail.html', {'task': task})
