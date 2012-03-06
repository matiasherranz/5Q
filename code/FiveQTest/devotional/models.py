# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager


class Devotional(models.Model):
    date = models.DateField("Date of the devotional.")
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000, null=True, blank=True)
    tags = TaggableManager()

    def __unicode__(self):
        return "%s - %s" % (self.title, self.date)
