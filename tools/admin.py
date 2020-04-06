from django.contrib import admin

# Register your models here.
from tools.models import Person, Projects


class ProjectsAdmin(admin.ModelAdmin):
    fields = ("name", "leader", "tester")
    list_display = ["id", "name", "leader", "tester"]


admin.site.register(Person)
admin.site.register(Projects)
