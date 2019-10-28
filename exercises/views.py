from django.shortcuts import render
from django.views import View

from exercises.models import Mark

from exercises.core.func import send_udp_datagram


class ImportBase(View):
    template = None
    page_title = None

    def get(self, request):
        return render(request, self.template, {'page_title': self.page_title})


class ImportData(ImportBase):
    template = 'import.html'
    page_title = 'Test import'


class ImportRequest(ImportBase):
    template = 'import-request.html'
    page_title = 'Request import'

    def post(self, request):
        context = {'page_title': self.page_title}

        header_ip = request.POST.get('header_ip')
        header_port = request.POST.get('header_port')
        if not (header_ip and header_port):
            context['message'] = 'header_ip or header_port is missing'
            return render(request, self.template, context)

        header_port = int(header_port)

        send_udp_datagram(header_ip, header_port)
        context['message'] = 'UDP datagram was sent'
        return render(request, self.template, context)


class Index(ImportBase):
    template = 'index.html'
    page_title = 'Программный иммитатор КОС-УД'


class ExercisesTable(View):

    def get(self, request):
        context = {
            'page_title': 'Таблица результатов',
            'items': Mark.objects.all().order_by('date').values('exercise__title', 'value', 'date',
                                                                'user_role', 'user__studyprofile__rank',
                                                                'user__studyprofile__studygroup__name',
                                                                'user__first_name', 'user__last_name')
        }
        return render(request, 'exercises-table.html', context)
