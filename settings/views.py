from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import GenderChoice
from .serializers import (GenderChoiceSerializer, TokenSerializer)


class TokenCreateView(APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_201_CREATED)
            
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class GenderChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GenderChoice.objects.all()
    serializer_class = GenderChoiceSerializer
