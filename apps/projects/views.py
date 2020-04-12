from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from projects.models import Projects
from projects.serializer import ProjectModelSerializer, ProjectNameSerializer, InterfaceNameSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    """
    list:
    获取所有项目信息
    update:
    修改项目
    create:
    创建项目
    destroy:
    删除项目
    retrieve:
    查看项目具体信息
    """
    queryset = Projects.objects.filter(is_delete=False)
    serializer_class = ProjectModelSerializer
    ordering_fields = ["name", "id"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "leader", "tester"]
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance: Projects):
        instance.is_delete = True
        instance.save()

    @action(methods=["get"], detail=False)
    def names(self, request, *args, **kwargs):
        projects = self.get_queryset()
        serializer = ProjectNameSerializer(instance=projects, many=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=False)
    def interfaces(self, request, *args, **kwargs):
        interfaces = self.get_object()
        serializer = InterfaceNameSerializer(instance=interfaces)
        return Response(serializer.data)
