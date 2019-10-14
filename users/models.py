from django.contrib.auth.models import AbstractUser
from django.db import models


class StudyGroup(models.Model):
    name = models.CharField('name', max_length=512)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        db_table = 'users__studygroup'


class User(AbstractUser):
    rank = models.CharField('rank', max_length=512, blank=True, null=True)
    studygroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='group', blank=True, null=True)

    @property
    def fullname(self):
        return f'{self.last_name} {self.first_name}'

    def __str__(self):
        return f'{self.username}: {self.fullname}'
