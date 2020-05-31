from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class Pediatrician(models.Model):
    name = models.CharField(verbose_name=_('name'), blank=False, null=False, max_length=64)
    email = models.EmailField(verbose_name=_('email'), unique=True, null=False)

    class Meta:
        verbose_name = _('pediatrician')
        verbose_name_plural = _('pediatricians')

    def __str__(self):
        return self.name

class Appointment(models.Model):
    pediatrician = models.ForeignKey(verbose_name=_('pediatrician'), to=Pediatrician, related_name='appointments', on_delete=models.CASCADE)
    commentary = models.CharField(verbose_name=_('commentary'), blank=True, null=True, max_length=512)
    datetime = models.DateTimeField(verbose_name=_('datetime'), null=False)
    user = models.ForeignKey(verbose_name=_('user'), to=get_user_model(), related_name='appointments', on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = _('appointment')
        verbose_name_plural = _('appointments')

    def __str__(self):
        return '{pediatrician} - {user} at {datetime}'.format_map({
            "pediatrician": self.pediatrician.name,
            "user": self.user.username,
            "datetime": self.datetime
        }) 