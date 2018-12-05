# Generated by Django 2.1.2 on 2018-10-12 14:18
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.db import migrations, models
import django_celery_beat.validators
import timezone_field.fields


class Migration(migrations.Migration):
    replaces = [
        ('django_celery_beat', '0005_add_solarschedule_events_choices'),
        ('django_celery_beat', '0006_auto_20180210_1226'),
        ('django_celery_beat', '0006_auto_20180322_0932'),
        ('django_celery_beat', '0007_auto_20180521_0826'),
        ('django_celery_beat', '0008_auto_20180914_1922'),
    ]

    dependencies = [
        ('django_celery_beat', '0004_auto_20170221_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarschedule',
            name='event',
            field=models.CharField(
                choices=[('dawn_astronomical', 'dawn_astronomical'),
                         ('dawn_civil', 'dawn_civil'),
                         ('dawn_nautical', 'dawn_nautical'),
                         ('dusk_astronomical', 'dusk_astronomical'),
                         ('dusk_civil', 'dusk_civil'),
                         ('dusk_nautical', 'dusk_nautical'),
                         ('solar_noon', 'solar_noon'), ('sunrise', 'sunrise'),
                         ('sunset', 'sunset')], max_length=24,
                verbose_name='event'),
        ),
        migrations.AlterModelOptions(
            name='crontabschedule',
            options={
                'ordering': ['month_of_year', 'day_of_month', 'day_of_week',
                             'hour', 'minute', 'timezone'],
                'verbose_name': 'crontab', 'verbose_name_plural': 'crontabs'},
        ),
        migrations.AlterModelOptions(
            name='crontabschedule',
            options={
                'ordering': ['month_of_year', 'day_of_month', 'day_of_week',
                             'hour', 'minute', 'timezone'],
                'verbose_name': 'crontab', 'verbose_name_plural': 'crontabs'},
        ),
        migrations.AddField(
            model_name='crontabschedule',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(
                default=getattr(settings, 'TIME_ZONE', 'UTC')
            ),
        ),
        migrations.AddField(
            model_name='periodictask',
            name='one_off',
            field=models.BooleanField(default=False,
                                      verbose_name='one-off task'),
        ),
        migrations.AddField(
            model_name='periodictask',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True,
                                       verbose_name='start_time'),
        ),
        migrations.AlterField(
            model_name='crontabschedule',
            name='day_of_month',
            field=models.CharField(default='*', max_length=124, validators=[
                django_celery_beat.validators.day_of_month_validator],
                verbose_name='day of month'),
        ),
        migrations.AlterField(
            model_name='crontabschedule',
            name='day_of_week',
            field=models.CharField(default='*', max_length=64, validators=[
                django_celery_beat.validators.day_of_week_validator],
                verbose_name='day of week'),
        ),
        migrations.AlterField(
            model_name='crontabschedule',
            name='hour',
            field=models.CharField(default='*', max_length=96, validators=[
                django_celery_beat.validators.hour_validator],
                verbose_name='hour'),
        ),
        migrations.AlterField(
            model_name='crontabschedule',
            name='minute',
            field=models.CharField(default='*', max_length=240, validators=[
                django_celery_beat.validators.minute_validator],
                verbose_name='minute'),
        ),
        migrations.AlterField(
            model_name='crontabschedule',
            name='month_of_year',
            field=models.CharField(default='*', max_length=64, validators=[
                django_celery_beat.validators.month_of_year_validator],
                verbose_name='month of year'),
        ),
    ]
