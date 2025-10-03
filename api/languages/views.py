from rest_framework import generics
from portfolio.permissions import IsAdminUserOrReadOnly
from .models import Language
from .serializers import LanguageSerializer

# Create your views here.

class LanguageList(generics.ListCreateAPIView):
    """
    This view fetches all the language objects and
    returns them to the user
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(self.request.user)

class LanguageDetail(generics.RetrieveDestroyAPIView):
    """
    This view fetches specific language objects and
    returns them to the user
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUserOrReadOnly]
