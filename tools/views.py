# coding=utf-8
import json

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import Projects
from tools.serializer import ProjectSerializer, ProjectModelSerialzer


class IndexView(View):
    def get(self, request):
        for i in range(10):
            project = Projects(name="项目1" + str(i), leader="张三" + str(i), tester="李四" + str(i), developer="王五" + str(i),
                               publish_app="App" + str(i), desc="项目简介" + str(i))
            project.save()
        pass
        return render(request, "demo.html", locals())


class ProjectsList(GenericAPIView):
    queryset = Projects.objects.all().order_by("id")
    serializer_class = ProjectModelSerialzer
    ordering_fields = ["name", "leader", "id"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "leader", "tester"]

    def get(self, request):
        projects = self.get_queryset()
        projects = self.filter_queryset(projects)
        page = self.paginate_queryset(projects)
        if page:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(instance=projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        json_data = request.body.decode("utf-8")
        python_data = json.loads(json_data, encoding="utf-8")
        serializer = ProjectSerializer(data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=201)


class ProjectsDetail(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerialzer

    def get(self, request, pk):
        project = self.get_object()
        serializer = self.get_serializer(instance=project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        project = self.get_object()
        json_data = request.body.decode("utf-8")
        python_data = json.loads(json_data, encoding="utf-8")
        serializer = self.get_serializer(instance=project, data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data, safe=False, status=200)

    def delete(self, request, pk):
        project = self.get_object()
        project.delete()
        return Response(None, safe=False, status=204)
