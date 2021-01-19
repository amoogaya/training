from django.contrib import admin
from .models import (RegisterRequestPendingEmployeeReview,
                     RegisterRequestRejectedBYEmployee,
                     RegisterRequestPendingLeaderReview,
                     RegisterRequestRejected,
                     RegisterRequestApproved, )


# Register your models here.
admin.site.register(RegisterRequestPendingEmployeeReview)
admin.site.register(RegisterRequestRejectedBYEmployee)
admin.site.register(RegisterRequestPendingLeaderReview)
admin.site.register(RegisterRequestRejected)
admin.site.register(RegisterRequestApproved)
