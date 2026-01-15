from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        elif request.user.is_teacher:
            return redirect('teacher_dashboard')
        elif request.user.is_student:
            return redirect('student_dashboard')
    return render(request, 'home.html')

@login_required
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'core/teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')
