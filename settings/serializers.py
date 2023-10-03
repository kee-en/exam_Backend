from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import GenderChoice

User = get_user_model()


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class GenderChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderChoice
        fields = "__all__"
