from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from training.settings import EMAIL_HOST_USER


# Create your views here.
def send_email_to_user(request, subject, msg, to):
    result_send_email = send_mail(subject, msg, EMAIL_HOST_USER, to)
    if result_send_email == 1:
        msg = "Mail Sent success"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)
