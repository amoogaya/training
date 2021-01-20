from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(verbose_name=_('first name'), max_length=200, blank=False)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=200, blank=False)
    username = models.CharField(verbose_name=_('username'), max_length=150, unique=True)
    password = models.CharField(verbose_name=_('password'), max_length=150)
    email = models.EmailField(verbose_name=_('email'), blank=True, null=True)
    is_staff = models.BooleanField(verbose_name=_('is_staff'), default=False)

    class Meta:
        verbose_name = 'my user'
        verbose_name_plural = 'my users'


class Client(User):
    plan = models.TextField(help_text='enter your plan')
    balance = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
