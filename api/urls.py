from django.urls import path, include
from portfolio.views import api_root

urlpatterns = [
    path('', api_root, name='api'),
    path('projects/', include('api.projects.urls'), name='projects'),
    path('users/', include('api.accounts.urls'), name='users'),
]
