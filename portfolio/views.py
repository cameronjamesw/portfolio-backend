from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'projects': reverse('project-list', request=request, format=format),
        'languages': reverse('language-list', request=request, format=format),
        'libraries': reverse('libraries-list', request=request, format=format),
        'frameworks': reverse('framework-list', request=request, format=format)
    })


@api_view()
@permission_classes([AllowAny])
def top_route(request, format=None):
    return Response({
        'message': 'Top root for Portfolio API',
        'api': reverse('api', request=request, format=format),
    }
    )
