# encoding: utf-8

"""
@author: shaoyanyan
@file: serializer.py
@time: 2020/4/12 22:40
@ide: pycharm

"""
from rest_framework import serializers

from debugtalks.models import Debugtalks
from interfaces.models import Interfaces
from projects.models import Projects


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ("update_time", "is_delete")
        extra_kwargs = {
            "create_time": {
                "read_only": True
            }
        }

    def create(self, validated_data):
        project_obj = super().create(validated_data)
        Debugtalks.objects.create(project=project_obj)
        return project_obj


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "name")


class InterfaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ("id", "name", "tester")


class InterfaceByProjectIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "name", "tester")


class InterfaceByProjectIdSerializer(serializers.ModelSerializer):
    interfaces_set = InterfaceNameSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ("id", "interfaces_set")
