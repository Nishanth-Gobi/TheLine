from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserCreateForm(UserCreationForm):
    fields = ("username", "password1", "password2")
    model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields[0].label = "Username"
