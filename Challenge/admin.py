from django.contrib import admin

from .models import DayTask, WeeklyChallenge, UserChallenge


@admin.register(DayTask)
class DayTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'day_number']
    ordering = ['day_number']


@admin.register(WeeklyChallenge)
class WeeklyChallengeAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date']
    filter_horizontal = ['tasks']


@admin.register(UserChallenge)
class UserChallengeAdmin(admin.ModelAdmin):
    list_display = ['user', 'challenge', 'join_date']
    list_filter = ['challenge', 'user']
    search_fields = ['user__username', 'challenge__title']
