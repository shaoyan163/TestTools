# encoding: utf-8

"""
@author: shaoyanyan
@file: base_model.py
@time: 2020/4/12 19:01
@ide: pycharm

"""
from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除", help_text="逻辑删除")

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = "BaseModel"
