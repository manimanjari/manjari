# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 07:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doit', '0019_auto_20160627_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user_info',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
