from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from users.models import StudyProfile, StudyGroup


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
                (_('permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
                (_('personal info'), {'fields': ('first_name', 'last_name')}),
            )

    def fullname(self, obj):
        return f'{obj.username}: {obj.last_name} {obj.first_name}'
    fullname.allow_tags = True
    fullname.short_description = _("full name")

    def rank(self, obj):
        return obj.studyprofile.rank
    rank.allow_tags = True
    rank.short_description = _("rank")

    def studygroup(self, obj):
        if obj.studyprofile.studygroup:
            return obj.studyprofile.studygroup.name
        return '-'
    studygroup.allow_tags = True
    studygroup.short_description = _("study group")

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AdminUser, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = (InlineStudyProfile,)
        return super(AdminUser, self).change_view(*args, **kwargs)


admin.site.unregister(User)
admin.site.register(User, AdminUser)
