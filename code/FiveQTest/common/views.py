# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.core.urlresolvers import reverse


@login_required
def render_dashboard(request):
    """
    Render project dashboard.
    """
    links = {'Django admin': reverse('admin:index'),
             'Logout': reverse('auth_logout'),
             'List and search devotionals by date': reverse('view_devotionals'),
            }

    return render_to_response('common/dashboard.html',
                              {'links': links},
                              context_instance=RequestContext(request))
