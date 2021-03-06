# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-26 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0012_question_testcases'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('speaker', models.TextField()),
                ('registration_link', models.CharField(max_length=300)),
            ],
        ),
    ]
