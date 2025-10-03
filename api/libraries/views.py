from django.shortcuts import render
from rest_framework import generics
from portfolio.permissions import IsAdminUserOrReadOnly
from .models import Library
from .serializers import LibrarySerializer

# Create your views here.

class LibraryList(generics.ListCreateAPIView):
    """
    This view retrieves all of the libraries and displays
    the results to the users
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LibraryDetail(generics.RetrieveDestroyAPIView):
    """
    This view retrieves specific libraries and displays
    them to the users
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAdminUserOrReadOnly]
