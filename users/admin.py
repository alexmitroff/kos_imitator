from django.contrib import admin
from users.models import StudyProfile, StudyGroup
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


@admin.register(StudyGroup)
class AdminStudyGroup(admin.ModelAdmin):
    search_fields = ('name',)


class InlineStudyProfile(admin.StackedInline):
    model = StudyProfile
    can_delete = False


class AdminUser(BaseUserAdmin):
    list_display = ('fullname', 'email', 'rank', 'studygroup', 'is_staff')
    fieldsets = (
                ( None, {'fields': ('username', 'password')}),
                ('permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
                ('personal info', {'fields': ('first_name', 'last_name')}),
            )

    def fullname(self, obj):
        return f'{obj.username}: {obj.last_name} {obj.first_name}'

    def rank(self, obj):
        return obj.studyprofile.rank

    def studygroup(self, obj):
        return obj.studyprofile.studygroup.name

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AdminUser, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = (InlineStudyProfile,)
        return super(AdminUser, self).change_view(*args, **kwargs)


admin.site.unregister(User)
admin.site.register(User, AdminUser)
