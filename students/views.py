from django.contrib.auth.views import LoginView
from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentProfile
from .serializer import StudentProfileSerializer

# Create your views here.


class StudentProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
