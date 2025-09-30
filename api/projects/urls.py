from django.urls import path
from .views import project_detail, project_list

urlpatterns = [
    path('projects/', project_list),
    path('projects/<int:pk>', project_detail)
]