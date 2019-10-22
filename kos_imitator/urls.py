from django.contrib import admin
from django.urls import path, include
from users.api.views import Export
from exercises.api.views import Import
from exercises.views import ImportData, ImportRequest, Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('import/', ImportData.as_view(), name='import-test'),
    path('request/', ImportRequest.as_view(), name='import-request'),
    path('', include('users.urls')),

    path('moodle/local/ittrainer/export.php', Export.as_view(), name='export'),
    path('moodle/local/ittrainer/import.php', Import.as_view(), name='import'),
    path('moodle/', admin.site.urls),
]
