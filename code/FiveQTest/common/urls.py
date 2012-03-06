# -*- coding: utf-8 *-*
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('common',
    url(r'^/dashboard/', 'views.render_dashboard'),
)
