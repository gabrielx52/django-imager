"""Imager Images forms."""
from django import forms

from imager_images.models import Album, Photo


class NewAlbumForm(forms.ModelForm):
    """New album form."""

    class Meta:
        """Meta."""

        model = Album
        exclude = ['user', 'date_uploaded', 'date_published', 'date_modified']


class NewPhotoForm(forms.ModelForm):
    """New photo form."""

    class Meta:
        """Meta."""

        model = Photo
        exclude = ['user', 'date_published', 'date_modified', 'date_uploaded']
