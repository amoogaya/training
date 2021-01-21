from django.contrib import admin
from .views import send_email_to_user
from .models import (RegisterRequestPendingEmployeeReview,
                     RegisterRequestRejectedBYEmployee,
                     RegisterRequestPendingLeaderReview,
                     RegisterRequestRejected,
                     RegisterRequestApproved,
                     RegisterRequestLog)


# Register your models here.
class RegisterRequestPendingEmployeeReviewAdmin(admin.ModelAdmin):
    actions = ['pending_leader_review', 'rejected_by_employee']

    def pending_leader_review(self, request, queryset):
        for obj in queryset:
            RegisterRequestLog.objects.create(
                register_request_id=obj.id,
                flag='pending_leader_review',
            )
        queryset.update(flag='pending_leader_review')

    def rejected_by_employee(self, request, queryset):
        for obj in queryset:
            RegisterRequestLog.objects.create(
                register_request_id=obj.id,
                flag='rejected_by_employee',
            )
        queryset.update(flag='rejected_by_employee')

    pending_leader_review.short_description = 'assign it to leader to review'
    rejected_by_employee.short_description = 'rejected the request'


class RegisterRequestPendingLeaderReviewAdmin(admin.ModelAdmin):
    actions = ['approved', 'rejected']

    def approved(self, request, queryset):
        for obj in queryset:
            RegisterRequestLog.objects.create(
                register_request_id=obj.id,
                flag='approved',
            )
            print(obj.register_request.email)
            n = send_email_to_user(request,
                                   'register request is approved',
                                   'congratulations your register request is approved',
                                   ['aya.goomaa@gmail.com']
                                   )
            obj.register_request.status = 'approved'
        # [obj.register_request.email, ]
        queryset.update(flag='approved')

    def rejected(self, request, queryset):
        for obj in queryset:
            RegisterRequestLog.objects.create(
                register_request_id=obj.id,
                flag='rejected',
            )

            n = send_email_to_user(request,
                                   'register request is rejected',
                                   'we are sorry your register request is rejected , for these reasones ',
                                   [obj.register_request.email, ],
                                   )
            obj.register_request.status = 'approved'

        queryset.update(flag='rejected')

    approved.short_description = 'approved the request'
    rejected.short_description = 'rejected the request'


admin.site.register(RegisterRequestPendingEmployeeReview,
                    RegisterRequestPendingEmployeeReviewAdmin)

admin.site.register(RegisterRequestPendingLeaderReview,
                    RegisterRequestPendingLeaderReviewAdmin)

admin.site.register(RegisterRequestRejectedBYEmployee)
admin.site.register(RegisterRequestRejected)
admin.site.register(RegisterRequestApproved)
admin.site.register(RegisterRequestLog)
