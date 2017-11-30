"""Imager profile app urls."""
from django.conf.urls import url

from imager_profile.views import profile_view, user_profile_view

urlpatterns = [
    url(r'^$', profile_view, name='profile'),
    url(r'^(?P<username>\w+)/$', user_profile_view, name='user_profile')
]
