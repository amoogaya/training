from django.contrib.auth.forms import UserCreationForm
from .models import Client


class UserForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'username', ]

