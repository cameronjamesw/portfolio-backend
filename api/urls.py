from django.urls import path, include

urlpatterns = [
    path('', include('api.projects.urls')),
    path('users/', include('api.accounts.urls')),
]
