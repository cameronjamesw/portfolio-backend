from django.urls import path
from .views import ProjectList, ProjectDetail

urlpatterns = [
    path('', ProjectList.as_view()),
    path('<int:pk>/', ProjectDetail.as_view()), 
]
