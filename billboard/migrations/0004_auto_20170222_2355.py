# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-22 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0003_auto_20170221_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]