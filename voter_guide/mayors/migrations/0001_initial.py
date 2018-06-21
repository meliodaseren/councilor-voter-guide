# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 07:51
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mayors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('birth', models.DateField(blank=True, null=True)),
                ('former_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=None, null=True, size=None)),
                ('identifiers', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=70, unique=True)),
                ('election_year', models.CharField(db_index=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('party', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('county', models.CharField(db_index=True, max_length=100)),
                ('contact_details', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('term_start', models.DateField(blank=True, null=True)),
                ('term_end', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('links', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('social_media', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('platform', models.TextField(blank=True, null=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('mayor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='each_terms', to='mayors.Mayors', to_field='uid')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='terms',
            unique_together=set([('mayor', 'election_year')]),
        ),
    ]