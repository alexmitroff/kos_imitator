import json
from datetime import datetime as dt

from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from exercises.api.authentication import CsrfExemptSessionAuthentication
from exercises.models import Exercise, Mark


class Import(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    parser_classes = (MultiPartParser, FileUploadParser)

    def post(self, request):
        json_file = request.data.get('file')
        if not json_file:
            return Response({'message': 'server did not receive file'}, status=400)

        json_data = json.loads(json_file.read())

        trainings = json_data.get('trainings')
        if not trainings:
            return Response({'message': 'There are no training in file'}, status=400)

        for training in trainings:
            training_id = training['training_id']
            training_title = training['training_title']
            training_date = dt.fromtimestamp(training['training_date'])
            user_id = training['user_id']
            user_role = training['user_role']
            user_mark = training['user_mark']
            comment = training['comment']

            exercise, e_created = Exercise.objects.get_or_create(id=training_id, defaults={'title': training_title})

            user = User.objects.filter(id=user_id).first()
            if not user:
                return Response({'message': f'There is not student with {user_id} id'}, status=400)

            mark, m_created = Mark.objects.update_or_create(exercise=exercise,
                                                            user=user,
                                                            user_role= user_role,
                                                            defaults={
                                                                'value': user_mark,
                                                                'date': training_date,
                                                                'comment': comment
                                                            }
                                                            )




        return Response({'starts': True}, status=200)
