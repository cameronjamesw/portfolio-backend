from django.urls import path, include

urlpatterns = [
    path('', include('api.projects.urls')),
]
