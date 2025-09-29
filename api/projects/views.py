from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

@csrf_exempt
def project_list(request):
    """
    Lists all the projects, or creates a new one
    """

    if request.method == "GET":
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def project_detail(request, pk):
    """
    Retrieve, update or delete a project
    """

    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = ProjectSerializer(project)
        return JSONParser(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, response=200)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        project.delete()
        return HttpResponse(status=204)
        