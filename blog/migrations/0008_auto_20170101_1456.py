# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 14:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_customuser_is_admin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('date',)},
        ),
        migrations.AlterModelTable(
            name='post',
            table=None,
        ),
    ]
