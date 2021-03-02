from django.contrib import admin
from tester_home.models.project import Project
from tester_home.models.module import Module


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'create_time', 'update_time']
    search_fields = ['name']
    list_filter = ['status']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name', 'description', 'status', 'create_time', 'update_time']
    search_fields = ['name']
    list_filter = ['status']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)