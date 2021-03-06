# Generated by Django 2.2.6 on 2019-10-17 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'verbose_name': 'упражнение', 'verbose_name_plural': 'упражнения'},
        ),
        migrations.AlterModelOptions(
            name='mark',
            options={'verbose_name': 'оценка', 'verbose_name_plural': 'оценки'},
        ),
        migrations.AlterField(
            model_name='exercise',
            name='title',
            field=models.CharField(max_length=512, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='комментарий'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='date',
            field=models.DateTimeField(verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Exercise', verbose_name='упражнение'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='user_role',
            field=models.CharField(max_length=128, verbose_name='роль'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='value',
            field=models.PositiveIntegerField(verbose_name='оценка'),
        ),
    ]
