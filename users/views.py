from django.shortcuts import render
from django.views import View

from users.models import StudyGroup
from django.contrib.auth.models import User

class UsersView(View):

    def get(self, request):
        context = {
            'page_title': 'Личный состав',
            'users': User.objects.exclude(is_staff=True, is_superuser=True).select_related('studyprofile')
        }
        return render(request, 'user-table.html', context)

class StudyGroupView(View):

    def get(self, request):
        context = {
            'page_title': 'Подразделения',
            'studygroups': StudyGroup.objects.all()
        }
        return render(request, 'group-table.html', context)