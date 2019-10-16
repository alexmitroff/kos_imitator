from django.db import models
from django.utils.translation import gettext as _


class Exercise(models.Model):
    title = models.CharField(_('title'), max_length=512)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('exercise')
        verbose_name_plural = _('exercises')


class Mark(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name=_('exercise'))
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user')
    user_role = models.CharField(_('role'), max_length=128)
    date = models.DateTimeField(_('date'))
    value = models.PositiveIntegerField(_('mark'))
    comment = models.TextField(_('comment'), blank=True, null=True)

    def __str__(self):
        return f'{self.exercise.title}: {self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name = _('mark')
        verbose_name_plural = _('marks')
