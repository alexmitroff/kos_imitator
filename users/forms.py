from django.forms import ModelForm
from users.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserForm(ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password"))

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'rank', 'studygroup')