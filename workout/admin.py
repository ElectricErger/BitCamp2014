from django.contrib import admin
from workout.models import ExerciseEvent

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,				{'fields': ['woType']}),
        ('Clock', 			{'fields': ['startTime', 'endTime']}),
        ('Timing', 			{'fields': ['elapsedTime']})

    ]
    list_display = ('id', 'woType' ,'startTime')


admin.site.register(ExerciseEvent, EventAdmin)