# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-27 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0013_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
