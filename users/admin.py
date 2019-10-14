from django.contrib import admin
from users.models import User, StudyGroup


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('studygroup',)
    search_fields = ('first_name', 'last_name', 'username', 'studygroup__name')
    list_display = ('__str__', 'email', 'rank', 'studygroup')

    def studygroup(self, obj):
        if obj.studygroup:
            return obj.studygroup.name
        return '-'


@admin.register(StudyGroup)
class StydyGroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)
