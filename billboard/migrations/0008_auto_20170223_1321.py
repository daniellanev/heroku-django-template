# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0007_auto_20170223_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billboard.Message'),
        ),
    ]
