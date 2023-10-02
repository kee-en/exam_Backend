from django.shortcuts import render
from rest_framework import viewsets
from .models import GenderChoice
from .serializers import GenderChoiceSerializer


class GenderChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GenderChoice.objects.all()
    serializer_class = GenderChoiceSerializer
