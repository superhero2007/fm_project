# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-06 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvps', '0004_auto_20170805_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='payout_id',
            field=models.CharField(default='', max_length=100, verbose_name='Stripe Payout Id'),
            preserve_default=False,
        ),
    ]
