# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Devotional


@login_required
def view_devotionals(request):
    """
    Render a form that accepts a date and let's the user filter the matching
    devotionals for the given date.
    """
    results_found, was_post = True, False
    if request.POST:
        date = request.POST.get('devotional_date')
        devotionals = Devotional.objects.filter(date=date)
        was_post = True
    else:
        devotionals = Devotional.objects.all().order_by('-date')

    results_found = devotionals.count() > 0
    return render_to_response('devotional/view_devotionals.html',
                              {'devotionals': devotionals,
                               'results_found': results_found,
                               'was_post': was_post},
                              context_instance=RequestContext(request))


@login_required
def render_words_count(request):
    """
    Count the total number of words in the devotionals and render it.
    """
    count = 0
    try:
        count = sum([len(d.body.split(None)) for d in Devotional.objects.all()])
    except:
        pass

    return render_to_response('devotional/view_word_count.html',
                              {'count': count},
                              context_instance=RequestContext(request))
