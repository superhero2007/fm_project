# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-04 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0003_chef_legal_entity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='legal_entity_type',
            field=models.CharField(choices=[('individual', 'individual'), ('company', 'company')], default='individual', max_length=10),
        ),
    ]
