from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
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
            'thumbnail',
            'created_at',
            'updated_at'
        ]
