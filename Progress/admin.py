from django.contrib import admin

from django.contrib import admin
from WEB.models import TaskCategory


@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color')
    search_fields = ('name', 'description')
