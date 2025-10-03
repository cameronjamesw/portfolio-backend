from rest_framework import serializers
from .models import Framework

class FrameworkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Framework
        fields = [
            'id',
            'owner',
            'name',
            'created_at'
        ]
