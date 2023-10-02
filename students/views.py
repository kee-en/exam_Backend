from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.

#Custom login view for students
class StudentLoginView(LoginView):
    template_name = "students/login.html"
    redirect_authenticated_user = True