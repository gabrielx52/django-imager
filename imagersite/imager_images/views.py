"""Django profile app views."""
from django.contrib.auth.models import User
from django.views.generic import TemplateView


from imager_images.models import Album, Photo


class LibraryView(TemplateView):
    """Library view class based view."""

    def get_context_data(self, username=None):
        """Get context data for view."""
        user = User.objects.get(username=username)
        return {'user': user}


class PhotoView(TemplateView):
    """Photo view class based view."""

    def get_context_data(self, pk=None):
        """Get context data for view."""
        photo = Photo.objects.get(id=pk)
        return {'photo': photo}


class AlbumView(TemplateView):
    """Album view class based view."""

    def get_context_data(self, pk=None):
        """Get context data for view."""
        album = Album.objects.get(id=pk)
        return {'album': album}
