from django.urls import path
from users.views import UsersView, StudyGroupView
app_name = 'users'

urlpatterns = [
    path('students', UsersView.as_view(), name='list'),
    path('groups', StudyGroupView.as_view(), name='groups'),
]