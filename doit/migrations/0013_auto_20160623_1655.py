# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doit', '0012_auto_20160623_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
