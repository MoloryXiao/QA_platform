from django.contrib import admin
from apps.module.models import Module


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name', 'description', 'status', 'create_time', 'update_time']
    search_fields = ['name']
    list_filter = ['status']


admin.site.register(Module, ModuleAdmin)