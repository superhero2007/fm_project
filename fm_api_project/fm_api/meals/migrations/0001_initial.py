# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-30 04:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('serving_description', models.TextField()),
                ('servings_offered', models.IntegerField(default=2)),
                ('servings_purchased', models.IntegerField(default=0)),
                ('min_servings', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('serving_date', models.DateTimeField()),
                ('rsvp_date', models.DateTimeField()),
                ('accept_delivery', models.BooleanField(default=False)),
                ('accept_pickup', models.BooleanField(default=False)),
                ('accept_dine_in', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
    ]
