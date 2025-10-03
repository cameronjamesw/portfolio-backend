from django.urls import path
from .views import LanguageList, LanguageDetail

urlpatterns = [
    path('', LanguageList.as_view(), name="language-list"),
    path('<int:pk>/', LanguageDetail.as_view(), name="language-detail")
]
