# -*- coding: utf-8 *-*
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('devotional',
    url(r'^view_devotionals/', 'views.view_devotionals',
            name='view_devotionals'),
    url(r'^view_words_count/', 'views.render_words_count',
            name='view_words_count'),
)
