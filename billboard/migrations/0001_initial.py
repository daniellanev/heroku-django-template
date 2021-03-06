# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(max_length=200)),
                ('message_text', models.CharField(max_length=500)),
                ('message_author', models.CharField(max_length=200)),
                ('message_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
