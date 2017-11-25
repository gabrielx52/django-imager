"""Django imager views."""
from django.shortcuts import render


def home_view(request, number=None):
    """View for the home page."""
    return render(request, 'imagersite/home.html')
