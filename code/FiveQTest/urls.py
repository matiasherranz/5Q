# -*- coding: utf-8 *-*
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Enabling the Django admin interface:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    # Project urls:
    url(r'^common', include('common.urls')),

    url(r'^', 'django.views.generic.simple.redirect_to',
        {'url': '/common/dashboard/'}),
    url(r'^/', 'django.views.generic.simple.redirect_to',
        {'url': '/common/dashboard/'}),


    # Django admin:
    url(r'^admin/', include(admin.site.urls)),

    # User authentication:
    url(r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
