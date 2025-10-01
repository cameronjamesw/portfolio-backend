from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserList(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CustomUser.objects.all()


class UserDetail(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CustomUser.objects.all()
