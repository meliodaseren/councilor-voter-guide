# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-20 09:38
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('councilors', '0002_auto_20170309_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='councilors',
            name='identifiers',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]