from django.urls import path
from .views import LibraryList, LibraryDetail

urlpatterns = [
    path('', LibraryList.as_view(), name="libraries-list"),
    path('<int:pk>', LibraryDetail.as_view(), name="libraries-detail")
]
