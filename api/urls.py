from django.urls import path, include
from portfolio.views import api_root

urlpatterns = [
    path('', api_root, name='api'),
    path('frameworks/', include('api.frameworks.urls'), name='frameworks'),
    path('languages/', include('api.languages.urls'), name='languages'),
    path('libraries/', include('api.libraries.urls'), name='libraries'),
    path('projects/', include('api.projects.urls'), name='projects'),
    path('users/', include('api.accounts.urls'), name='users'),
]
