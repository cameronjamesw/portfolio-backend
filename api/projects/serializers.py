from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Project
        fields = [
            'id',
            'user',
            'name',
            'description',
            'languages',
            'image',
            'live_link',
            'repo_link',
            'completion_date',
            'created_at',
            'updated_at'
        ]
