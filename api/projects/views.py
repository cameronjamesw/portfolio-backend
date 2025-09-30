from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions  import IsAuthenticatedOrReadOnly
from django.http import Http404
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.


class ProjectList(generics.ListCreateAPIView):
    """
    Lists all the projects, or creates a new one
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a project
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
