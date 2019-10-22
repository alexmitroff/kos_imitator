from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from users.api.serializers import SerializerStudyGroup, SerializerUser
from users.models import StudyGroup


class Export(APIView):

    def get(self, request):
        students = User.objects.filter(is_staff=False, is_superuser=False, is_active=True)
        students = students.select_related('studyprofile')
        students_ids = students.values_list('id', flat=True)
        groups = StudyGroup.objects.filter(group__user__in=students_ids).distinct('id')
        data = {
          "students": SerializerUser(students, many=True).data,
          "groups": SerializerStudyGroup(groups, many=True).data
        }
        return Response(data, status=200)
