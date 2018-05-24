# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-23 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180523_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=10, verbose_name='性别'),
        ),
    ]
