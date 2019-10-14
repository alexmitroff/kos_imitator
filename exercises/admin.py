from django.contrib import admin
from exercises.models import Exercise, Mark


admin.site.register(Exercise)


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_filter = ('exercise__title', 'user__studygroup__name')
    search_fields = ('exercise__title', 'user__studygroup__name', 'user__username', 'user__last_name')
    list_display = ('__str__', 'value', 'study_group', 'date')

    def study_group(self, obj):
        if obj.user.studygroup:
            return obj.user.studygroup.name
        return '-'
