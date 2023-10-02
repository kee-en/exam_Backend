from rest_framework import serializers
from .models import GenderChoice


class GenderChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderChoice
        fields = "__all__"
