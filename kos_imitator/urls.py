from django.contrib import admin
from django.urls import path
from users.api_views import Export

urlpatterns = [
    path('admin/', admin.site.urls),

    path('moodle/local/ittrainer/export.php', Export.as_view(), name='export'),
]
