"""Django profile app views."""
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from imager_images.models import Photo


class ProfileView(TemplateView):
    """User view class based view."""

    template_name = 'imager_profile/profile.html'


class GuestView(TemplateView):
    """Profile view class based view."""

    template_name = 'imager_profile/guest_profile.html'

    def get_context_data(self, username=None):
        """Get context data for view."""
        user = User.objects.get(username=username)
        photo = Photo.objects.order_by('?').first()
        return {'photo': photo,
                'user': user}
