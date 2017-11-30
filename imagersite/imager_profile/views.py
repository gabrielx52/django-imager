"""Django profile app views."""
from django.contrib.auth.models import User

from django.shortcuts import render

from imager_images.models import Photo


def profile_view(request, username=None):
    """View for profile."""
    return render(request, 'imager_profile/profile.html')


def user_profile_view(request, username=None):
    """View for profile."""
    user = User.objects.get(username=username)
    photo = Photo.objects.order_by('?').first()
    # import pdb; pdb.set_trace()
    return render(request, 'imager_profile/user_profile.html',
                  context={'user': user,
                           'photo': photo})
