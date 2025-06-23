from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth import views as auth_views

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('', redirect_to_login),  # Anasayfa login sayfasına yönlendirilecek
    path('tasks/', views.task_list, name='task_list'), 
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),

    # Login & Logout
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),


]
