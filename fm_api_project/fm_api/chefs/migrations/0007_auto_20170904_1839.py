# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-04 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0006_auto_20170815_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='dob',
            field=models.DateField(blank=True, help_text='Date of birth in format: yyyy-mm-dd. For example: 1994-07-13', verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='ssn_last_4',
            field=models.CharField(blank=True, help_text='Last 4 digits of Social Security Number', max_length=4),
        ),
    ]
