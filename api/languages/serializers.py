from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Language
        fields = [
            'id',
            'owner',
            'name',
            'created_at'
        ]
