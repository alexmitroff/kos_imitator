from django.db import models


class Exercise(models.Model):
    title = models.CharField('title', max_length=512)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'exercise'
        verbose_name_plural = 'exercises'


class Mark(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user')
    user_role = models.CharField('role', max_length=128)
    date = models.DateTimeField('date')
    value = models.PositiveIntegerField('mark')
    comment = models.TextField('comment', blank=True, null=True)

    def __str__(self):
        return f'{self.exercise.title}: {self.user.fullname}'

    class Meta:
        verbose_name = 'mark'
        verbose_name_plural = 'marks'
