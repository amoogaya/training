from django import forms
from .models import RegisterRequestPendingEmployeeReview


class RequestRegisterForm(forms.ModelForm):

    model = RegisterRequestPendingEmployeeReview
    exclude = [ 'status' ]


