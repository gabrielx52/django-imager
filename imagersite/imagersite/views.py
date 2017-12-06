"""Django imager views."""
from django.views.generic import TemplateView

from imager_images.models import Photo


class HomeView(TemplateView):
    """Home view class based view."""

    def get_context_data(self):
        """Get context data for view."""
        photo = Photo.objects.order_by('?').first()
        return {'photo': photo}
