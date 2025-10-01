from rest_framework import generics
from portfolio.permissions import IsAdminUserOrReadOnly
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserList(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = CustomUser.objects.all()


class UserDetail(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = CustomUser.objects.all()
