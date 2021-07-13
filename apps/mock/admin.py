from django.contrib import admin
from apps.project.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'create_time', 'update_time']
    search_fields = ['name']
    list_filter = ['status']


admin.site.register(Project, ProjectAdmin)