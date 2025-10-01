from rest_framework import serializers
from .models import CustomUser
from api.projects.models import Project


class CustomUserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'bio',
            'profile_image',
            'projects',
        ]
