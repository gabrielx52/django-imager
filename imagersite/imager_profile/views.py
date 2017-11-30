"""Django profile app views."""
from django.contrib.auth.models import User

from django.shortcuts import render

# from imager_profile.models import ImagerProfile


def profile_view(request, username=None):
    """View for profile."""
    return render(request, 'imager_profile/profile.html')


def user_profile_view(request, username=None):
    """View for profile."""
    user = User.objects.get(username=username)
    return render(request, 'imager_profile/user_profile.html',
                  context={'user': user})
