# -*- coding: utf-8 -*-
from django.db import models


class Keyword(models.Model):
    content = models.CharField(max_length=200)
    county = models.CharField(db_index=True, max_length=100)
    category = models.CharField(max_length=30)
    valid = models.BooleanField()
    hits = models.IntegerField()
    def __unicode__(self):
        return self.content

    class Meta:
        unique_together = ('content', 'county', 'category')
