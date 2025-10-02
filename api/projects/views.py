from rest_framework import generics
from portfolio.permissions import IsAdminUserOrReadOnly
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.


class ProjectList(generics.ListCreateAPIView):
    """
    Lists all the projects, or creates a new one
    """
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a project
    """
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
