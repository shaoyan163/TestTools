# encoding: utf-8

"""
@author: shaoyanyan
@file: serializer.py
@time: 2020/4/9 23:15
@ide: pycharm

"""
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

import user


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        label="确认密码",
        min_length=6,
        max_length=20,
        help_text="确认密码",
        error_messages={
            "min_length": "仅允许6-20个字符密码",
            "max_length": "仅允许6-20个字符密码"
        }
    )
    token = serializers.CharField(label="生成token", read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password", "email", "password_confirm",
                 "token")
        extra_kwargs = {
            "username": {
                "label": "用户名",
                "help_text": "用户名",
                "min_length": 6,
                "max_length": 20,
                "error_messages": {
                    "min_length": "仅允许6-20个字符密码",
                    "max_length": "仅允许6-20个字符密码",
                }
            },
            "email": {
                "label": "邮箱",
                "help_text": "邮箱",
                "write_only": True,
                "required": True,
            },
            "password": {
                "label": "密码",
                "help_text": "密码",
                "write_only": True,
                "min_length": 6,
                "max_length": 20,
                "error_messages": {
                    "min_length": "仅允许6-20个字符密码",
                    "max_length": "仅允许6-20个字符密码",
                }
            },
        }
    def create(self, validated_data):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user
