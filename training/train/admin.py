from django.contrib import admin
from .models import RegisterRequest
# Register your models here.


class RegisterRequestAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(RegisterRequest)
