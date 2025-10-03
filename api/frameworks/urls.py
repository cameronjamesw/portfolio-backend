from django.urls import path
from .views import FrameworkList, FrameworkDetail

urlpatterns = [
    path('', FrameworkList.as_view(), name="framework-list"),
    path('<int:id>/', FrameworkDetail.as_view(), name="framework-detail")
]
