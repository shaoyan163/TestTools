# encoding: utf-8

"""
@author: shaoyanyan
@file: serializer.py
@time: 2020/4/5 14:15
@ide: pycharm

"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from Interfaces.models import Interfaces
from tools.models import Projects


def is_unique_project_name(name):
    if "项目" not in name:
        raise serializers.ValidationError("项目名称必须包含项目")


class ProjectSerializer(serializers.Serializer):
    """
    创建项目序列化器类
    """
    # label相当于verbose_name
    id = serializers.IntegerField(label="ID", read_only=True)
    name = serializers.CharField(label="项目名称", max_length=200, help_text="项目名称",
                                 write_only=False,
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message="项目名称已存在"),
                                             is_unique_project_name])
    leader = serializers.CharField(label="负责人", max_length=50, help_text="负责人")
    tester = serializers.CharField(label="测试人员", max_length=50, help_text="测试人员")
    developer = serializers.CharField(label="开发人员", max_length=50, help_text="开发人员")
    publish_app = serializers.CharField(label="发布应用", max_length=50, help_text="发布应用")
    desc = serializers.CharField(label="简要描述", allow_null=True, allow_blank=True, default="", help_text="简要描述")

    def validate_name(self, value):
        if not value.endswith("项目"):
            raise serializers.ValidationError("项目必须以项目结尾")
        return value

    def validate(self, attrs):
        if "icon" not in attrs.get("name") and "icon" not in attrs.get("leader"):
            raise serializers.ValidationError("项目名称或者负责人必须包含icon")
        return attrs

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.leader = validated_data.get("leader")
        instance.tester = validated_data.get("tester")
        instance.developer = validated_data.get("developer")
        instance.publish_app = validated_data.get("publish_app")
        instance.desc = validated_data.get("desc")
        instance.save()
        return instance


class ProjectModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class ProjectNameSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "name")


class InterfacesNameSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ("id", "name", "tester")


class InterfacesByProjectIdSerialzer(serializers.ModelSerializer):
    interfaces_set = InterfacesNameSerialzer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ("id", 'interfaces_set')
