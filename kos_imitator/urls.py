from django.contrib import admin
from django.urls import path
from users.api.views import Export
from exercises.api.views import Import
from exercises.views import import_test

urlpatterns = [
    path('admin/', admin.site.urls),

    path('import/', import_test, name='import-test'),

    path('moodle/local/ittrainer/export.php', Export.as_view(), name='export'),
    path('moodle/local/ittrainer/import.php', Import.as_view(), name='import'),
]
