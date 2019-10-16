from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import SerializerStudyGroup, SerializerUser
from users.models import StudyGroup, User


class Export(APIView):

    def get(self, request):
        students = User.objects.filter(is_staff=False, is_superuser=False, is_active=True)
        groups = StudyGroup.objects.all()
        data = {
          "students": SerializerUser(students, many=True).data,
          "groups": SerializerStudyGroup(groups, many=True).data
        }
        return Response(data, status=200)
