from django.shortcuts import render
from rest_framework import generics
from portfolio.permissions import IsAdminUserOrReadOnly
from .models import Framework
from .serializers import FrameworkSerializer

# Create your views here.

class FrameworkList(generics.ListCreateAPIView):
    """
    This view retrieves all the frameworks and displays
    them to the user
    """
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FrameworkDetail(generics.RetrieveDestroyAPIView):
    """
    This view retrieves a specific frameworks and
    displays it to the user
    """
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer
    permission_classes = [IsAdminUserOrReadOnly]
