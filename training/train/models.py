from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class RegisterRequest(models.Model):
    REQUEST_STATUS = (
        ('waiting', _('waiting')),
        ('approved', _('approved')),
        ('rejected', _('rejected')),
    )
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    status = models.CharField(verbose_name=_('Request status'),
                              max_length=200,
                              default='waiting',
                              choices=REQUEST_STATUS)

    class Meta:
        verbose_name = _('Register request ')
        verbose_name_plural = _('Register requests ')
