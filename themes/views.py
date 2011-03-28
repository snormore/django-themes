from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

THEMES_MANAGER = getattr(settings, 'THEMES_MANAGER', None)

@login_required
def change(request, theme_id=None, template_name="themes/change.html"):
    if theme_id:
        profile = request.user.get_profile()
        profile.theme = theme_id
        profile.save()
        current_theme_id = theme_id
        return redirect('themes_change')
    else:
        current_theme_id = request.user.get_profile().theme
    return direct_to_template(request, template_name, {'themes': THEMES_MANAGER.themes, 'current_theme_id': current_theme_id})