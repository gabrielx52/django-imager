"""Imager profile app urls."""
from django.conf.urls import url

from imager_profile.views import GuestView, ProfileView

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile'),
    url(r'^(?P<username>\w+)/$', GuestView.as_view(), name='user_profile')
]
