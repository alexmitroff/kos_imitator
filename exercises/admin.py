from django.contrib import admin
from exercises.models import Exercise, Mark


admin.site.register(Exercise)


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'study_group', 'user_role', 'value', 'date')
    list_filter = ('exercise__title', 'user__studyprofile__studygroup__name')
    search_fields = ('exercise__title', 'user__studyprofile__studygroup__name', 'user__username', 'user__last_name')
    readonly_fields = ('exercise', 'user_fullname', 'date')
    fieldsets = (
        (None, {'fields': ('date', 'exercise', 'user_fullname', 'user_role', 'value', 'comment')}),
    )

    def study_group(self, obj):
        if obj.user.studyprofile.studygroup:
            return obj.user.studyprofile.studygroup.name
        return '-'

    def user_fullname(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name}'
