# -*- coding: utf-8 *-*
from django.contrib import admin

from models import Devotional


class DevotionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    search_fields = ('id', 'title', 'date')

admin.site.register(Devotional, DevotionalAdmin)
