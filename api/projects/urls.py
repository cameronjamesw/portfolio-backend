from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import project_detail, project_list

urlpatterns = [
    path('projects/', project_list),
    path('projects/<int:pk>', project_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
