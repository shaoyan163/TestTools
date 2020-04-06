# coding=utf-8
import json

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, mixins, response
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action

from tools.models import Projects
from tools.serializer import ProjectSerializer, ProjectModelSerialzer, ProjectNameSerialzer, \
    InterfacesByProjectIdSerialzer


class IndexView(View):
    def get(self, request):
        for i in range(10):
            project = Projects(name="项目1" + str(i), leader="张三" + str(i), tester="李四" + str(i), developer="王五" + str(i),
                               publish_app="App" + str(i), desc="项目简介" + str(i))
            project.save()
        pass
        return render(request, "demo.html", locals())


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all().order_by("id")
    serializer_class = ProjectModelSerialzer
    ordering_fields = ["name", "leader", "id"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "leader", "tester"]

    @action(methods=["get"], detail=False)
    def names(self, request, *args, **kwargs):
        projects = self.get_queryset()
        serializer = ProjectNameSerialzer(instance=projects, many=True)
        return Response(serializer.data)

    @action(methods=["get"],detail=False)
    def interfaces(self, request, *args, **kwargs):
        interfaces = self.get_object()
        serializer = InterfacesByProjectIdSerialzer(instance=interfaces)
        return Response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
    #
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectsList(generics.ListCreateAPIView):
    queryset = Projects.objects.all().order_by("id")
    serializer_class = ProjectModelSerialzer
    ordering_fields = ["name", "leader", "id"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "leader", "tester"]

    # def get(self, request, *args, **kwargs):
    # projects = self.get_queryset()
    # projects = self.filter_queryset(self.get_queryset())
    # page = self.paginate_queryset(projects)
    # if page:
    #     serializer = self.get_serializer(instance=page, many=True)
    #     return self.get_paginated_response(serializer.data)
    # serializer = self.get_serializer(instance=projects, many=True)
    # return Response(serializer.data)
    # return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    # json_data = request.body.decode("utf-8")
    # python_data = json.loads(json_data, encoding="utf-8")
    # serializer = ProjectSerializer(data=python_data)
    # try:
    #     serializer.is_valid(raise_exception=True)
    # except Exception as e:
    #     return JsonResponse(serializer.errors)
    # serializer.save()
    # return JsonResponse(serializer.data, safe=False, status=201)
    # return self.create(request, *args, **kwargs)


class ProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerialzer

    # def get(self, request, *args, **kwargs):
    # project = self.get_object()
    # serializer = self.get_serializer(instance=project)
    # return Response(serializer.data, status=status.HTTP_200_OK)
    # return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    # project = self.get_object()
    # json_data = request.body.decode("utf-8")
    # python_data = json.loads(json_data, encoding="utf-8")
    # serializer = self.get_serializer(instance=project, data=python_data)
    # try:
    #     serializer.is_valid(raise_exception=True)
    # except Exception as e:
    #     return Response(serializer.errors)
    # serializer.save()
    # return Response(serializer.data, safe=False, status=200)
    # return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    # project = self.get_object()
    # project.delete()
    # return Response(None, safe=False, status=204)
    # return self.destroy(request, *args, **kwargs)
