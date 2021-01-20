from django.db import models
from django.utils.translation import gettext_lazy as _
from train.models import RegisterRequest


# Create your models here.


class RegisterRequestState(models.Model):
    STATUS = (
        ('approved', _('Approved')),
        ('rejected_by_employee', _('Rejected by Employee')),
        ('rejected', _('Rejected')),
        ('pending_employee_review', _('Pending Employee Review')),
        ('pending_leader_review', _('Pending Leader Review')),
    )

    register_request = models.ForeignKey(RegisterRequest, on_delete=models.CASCADE)

    flag = models.CharField(max_length=200, choices=STATUS)

    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Register request state')
        verbose_name_plural = _('Register requests state')


class RegisterRequestPendingEmployeeReviewManager(models.Manager):
    def get_queryset(self):
        qs = super(RegisterRequestPendingEmployeeReviewManager, self).get_queryset()
        qs = qs.filter(flag='pending_employee_review')
        return qs


class RegisterRequestPendingEmployeeReview(RegisterRequestState):
    objects = RegisterRequestPendingEmployeeReviewManager()

    class Meta:
        verbose_name = _('Register request Pending employee review')
        verbose_name_plural = _('Register requests Pending employee review')
        proxy = True


class RegisterRequestPendingLeaderReviewManager(models.Manager):
    def get_queryset(self):
        qs = super(RegisterRequestPendingLeaderReviewManager, self).get_queryset()
        qs = qs.filter(flag='pending_leader_review')
        return qs


class RegisterRequestPendingLeaderReview(RegisterRequestState):
    objects = RegisterRequestPendingLeaderReviewManager()

    class Meta:
        verbose_name = _('Register request Pending Leader review')
        verbose_name_plural = _('Register requests Pending Leader review')
        proxy = True


class RegisterRequestRejectedBYEmployeeManager(models.Manager):
    def get_queryset(self):
        qs = super(RegisterRequestRejectedBYEmployeeManager, self).get_queryset()
        qs = qs.filter(flag='rejected_by_employee')
        return qs


class RegisterRequestRejectedBYEmployee(RegisterRequestState):
    objects = RegisterRequestRejectedBYEmployeeManager()

    class Meta:
        verbose_name = _('Register request rejected by employee')
        verbose_name_plural = _('Register requests rejected by employee')
        proxy = True


class RegisterRequestRejectedManager(models.Manager):
    def get_queryset(self):
        qs = super(RegisterRequestRejectedManager, self).get_queryset()
        qs = qs.filter(flag='rejected')
        return qs


class RegisterRequestRejected(RegisterRequestState):
    objects = RegisterRequestRejectedManager()

    class Meta:
        verbose_name = _('Register request rejected')
        verbose_name_plural = _('Register requests rejected')
        proxy = True


class RegisterRequestApprovedManager(models.Manager):
    def get_queryset(self):
        qs = super(RegisterRequestApprovedManager, self).get_queryset()
        qs = qs.filter(flag='approved')
        return qs


class RegisterRequestApproved(RegisterRequestState):
    objects = RegisterRequestApprovedManager()

    class Meta:
        verbose_name = _('Register request approved')
        verbose_name_plural = _('Register requests approved')
        proxy = True


class RegisterRequestLog(models.Model):
    STATUS = (
        ('approved', _('Approved')),
        ('rejected_by_employee', _('Rejected by Employee')),
        ('rejected', _('Rejected')),
        ('pending_employee_review', _('Pending Employee Review')),
        ('pending_leader_review', _('Pending Leader Review')),
    )

    register_request = models.ForeignKey(RegisterRequest, on_delete=models.CASCADE)

    flag = models.CharField(max_length=200, choices=STATUS)

    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Register request Log')
        verbose_name_plural = _('Register requests Log')
