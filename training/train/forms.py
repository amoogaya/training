from django.forms import ModelForm
from .models import RegisterRequest


class RequestRegisterForm(ModelForm):
    class Meta:
        model = RegisterRequest
        exclude = ['status']


