# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-07 12:05
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_add_verbose_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='intent',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
