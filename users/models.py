from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _


class StudyGroup(models.Model):
    name = models.CharField(_('name'), max_length=512)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('study group')
        verbose_name_plural = _('study groups')
        db_table = 'users__studygroup'


class StudyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(_('rank'), max_length=512, blank=True, null=True)
    studygroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='group', blank=True, null=True)

    class Meta:
        verbose_name = _('study profile')
        verbose_name_plural = _('study profiles')
        db_table = 'users__studyprofile'


@receiver(post_save, sender=User)
def create_study_profile(sender, instance, created, **kwargs):
    if created:
        StudyProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_study_profile(sender, instance, **kwargs):
    instance.studyprofile.save()
