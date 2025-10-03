from rest_framework import generics
from portfolio.permissions import IsAdminUserOrReadOnly
from .models import Language
from .serializers import LanguageSerializer

# Create your views here.

class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(self.request.user)

class LanguageDetail(generics.RetrieveDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUserOrReadOnly]
