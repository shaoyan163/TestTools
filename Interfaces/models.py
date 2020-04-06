from django.db import models


# Create your models here.

class Interfaces(models.Model):
    name = models.CharField(verbose_name="接口名称", max_length=200, unique=True, help_text="接口名称")
    leader = models.CharField(verbose_name="负责人", max_length=50, help_text="负责人")
    tester = models.CharField(verbose_name="测试人员", max_length=50, help_text="测试人员")
    desc = models.TextField(verbose_name="简要描述", blank=True, null=True, help_text="简要描述")
    project = models.ForeignKey("tools.Projects", on_delete=models.CASCADE, verbose_name="所属项目", help_text="所属项目")

    class Meta:
        db_table = "tb_interfaces"
        verbose_name = "接口"
        verbose_name_plural = "接口"
    def __str__(self):
        return self.name
