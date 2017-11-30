"""Django imager views."""
from django.shortcuts import render

from imager_images.models import Photo


def home_view(request, number=None):
    """View for the home page."""
    photo = Photo.objects.order_by('?').first()
    return render(request, 'imagersite/home.html', context={'photo': photo})
