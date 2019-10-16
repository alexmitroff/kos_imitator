# Generated by Django 2.2.6 on 2019-10-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studygroup',
            options={'verbose_name': 'учебная группа', 'verbose_name_plural': 'учебные группы'},
        ),
        migrations.AlterModelOptions(
            name='studyprofile',
            options={'verbose_name': 'учебный профиль', 'verbose_name_plural': 'учебные профиля'},
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='name',
            field=models.CharField(max_length=512, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='studyprofile',
            name='rank',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='ранг'),
        ),
    ]