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
        print("META from request")
        print(request.META.items())
        print('Import JSON Files!')
        json_file = request.data.get('file')
        if not json_file:
            print('server did not receive file')
            return Response({'message': 'server did not receive file'}, status=400)

        json_data = json.loads(json_file.read())

        trainings = json_data.get('trainings')
        if not trainings:
            print('There are no training in file')
            return Response({'message': 'There are no training in file'}, status=400)

        for training in trainings:
            training_id = training.get('training_id')
            if not training_id:
                print('training_id is missed')
                Response({'message': 'training_id is missed'}, status=400)

            training_title = training.get('training_title')
            if not training_title:
                print('training_title is missed')
                Response({'message': 'training_title is missed'}, status=400)

            training_date = training.get('training_date')
            if not training_date:
                print('training_date is missed')
                Response({'message': 'training_date is missed'}, status=400)
            training_date = dt.fromtimestamp(training_date)

            user_id = training.get('user_id')
            if not user_id:
                print('user_id is missed')
                Response({'message': 'user_id is missed'}, status=400)

            user_mark = training.get('user_mark')
            if not user_mark:
                print('user_mark is missed')
                Response({'message': 'user_mark is missed'}, status=400)

            user_role = training.get('user_role', '-')
            comment = training.get('comment', '-')

            exercise, e_created = Exercise.objects.get_or_create(id=training_id, defaults={'title': training_title})

            user = User.objects.filter(id=user_id).first()
            if not user:
                print(f'There is not student with {user_id} id')
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

        data = {'starts': True}
        return Response(data, status=200, content_type='application/json')
