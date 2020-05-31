from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from .models import Appointment, Pediatrician
from app.core.emails import send_mail_appointment


class AppointmentAdmin(admin.ModelAdmin):
    actions = ['send_message']

    def send_message(self, request, queryset):
        send = queryset.count()
        for appoiment in queryset:
            send_mail_appointment(appoiment.user.email, appoiment.datetime, appoiment.pediatrician)
            
        self.message_user(request, ngettext(
            '%(send)d email send successfully',
            '%(send)d emails send successfully',
            send,
        ) % {'send': send },
        messages.SUCCESS) 

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Pediatrician)
