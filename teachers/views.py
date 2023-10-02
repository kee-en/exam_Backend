from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.

class TeacherLoginView(LoginView):
    template_name = 'teacher/login.html'
    redirect_authenticated_user = True