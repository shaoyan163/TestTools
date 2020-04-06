from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(verbose_name="姓", max_length=30, help_text="姓")
    last_name = models.CharField(verbose_name="名字", max_length=30, help_text="名字")

    class Meta:
        db_table = "tb_person"
        verbose_name = "用户"
        verbose_name_plural = "用户"
    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(verbose_name="项目名称", max_length=200, unique=True, help_text="项目名称")
    leader = models.CharField(verbose_name="负责人", max_length=50, help_text="负责人")
    tester = models.CharField(verbose_name="测试人员", max_length=50, help_text="测试人员")
    developer = models.CharField(verbose_name="开发人员", max_length=50, help_text="开发人员")
    publish_app = models.CharField(verbose_name="发布应用", max_length=100, help_text="发布应用")
    desc = models.TextField(verbose_name="简要描述", blank=True, null=True, help_text="简要描述")

    class Meta:
        db_table = "tb_projects"
        verbose_name = "项目"
        verbose_name_plural = "项目"

    def __str__(self):
        return self.name
