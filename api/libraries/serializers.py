from rest_framework import serializers
from .models import Library

class LibrarySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Library
        fields = [
            'id',
            'owner',
            'name',
            'created_at'
        ]
