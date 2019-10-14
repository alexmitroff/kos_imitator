from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import SerializerStudyGroup, SerializerUser
from users.models import StudyGroup, User


class Export(APIView):

    def get(self, request):
        students = User.objects.all().select_related('studygroup')
        groups = StudyGroup.objects.all()
        data = {
          "students": SerializerUser(students, many=True).data,
          "groups": SerializerStudyGroup(groups, many=True).data
        }
        return Response(data, status=200)
