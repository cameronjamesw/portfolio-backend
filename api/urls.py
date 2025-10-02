from django.urls import path, include

urlpatterns = [
    path('projects/', include('api.projects.urls')),
    path('users/', include('api.accounts.urls')),
]
