from django.contrib import admin
from .models import WeeklyChallenge, Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 7


@admin.register(WeeklyChallenge)
class WeeklyChallengeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'start_date', 'end_date', 'completed']
    search_fields = ['user__username']
    inlines = [TaskInline]


admin.site.register(Task)
