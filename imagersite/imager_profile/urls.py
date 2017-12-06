"""Imager profile app urls."""
from django.conf.urls import url

from imager_profile.views import GuestView, ProfileView

urlpatterns = [
    url(r'^$',
        ProfileView.as_view(template_name='imager_profile/profile.html'),
        name='profile'),
    url(r'^(?P<username>\w+)/$',
        GuestView.as_view(template_name='imager_profile/guest_profile.html'),
        name='user_profile')
]
