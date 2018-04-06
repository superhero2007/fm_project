# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-05 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rsvps', '0003_auto_20170805_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='paid_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='rsvp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transfer', to='rsvps.Rsvp'),
        ),
    ]
