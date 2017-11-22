"""Imager profile model."""
from django.contrib.auth.models import User
from django.db import models


class ImagerProfile(models.Model):
    """Photographer profile model."""

    CAMERA_CHOICES = (('FL', 'Film'),
                      ('DG', 'Digital'),
                      ('PL', 'Polaroid'),
                      ('DG', 'Daguerreotype'))
    STYLE_CHOICES = (('PR', 'Portrait'),
                     ('SL', 'Still Life'),
                     ('NT', 'Nature'),
                     ('AB', 'Abstract'),
                     ('FS', 'Fashion'),
                     ('AD', 'Advertising'),
                     ('WL', 'Wildlife'),
                     ('WD', 'Wedding'),
                     ('BW', 'Black and White'),
                     ('MC', 'Macro'),
                     ('TP', 'Time Lapse'),
                     ('LS', 'Landscape'),
                     ('SP', 'Sports'))
    SERVICE_CHOICES = (('SS', 'Session'),
                       ('ED', 'Editing'),
                       ('CL', 'Coloring'),
                       ('PT', 'Printing'),
                       ('FR', 'Framing'),
                       ('AV', 'Advertising'),
                       ('TV', 'Travel'))
    location = models.CharField(max_length=180, blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile')
    website = models.URLField()
    fee = models.DecimalField(max_digits=10, decimal_places=2,
                              blank=True, null=True)
    phone = models.CharField(max_length=12)
    bio = models.TextField(max_length=500)
    camera = models.CharField(choices=CAMERA_CHOICES, max_length=2)
    photo_style = models.CharField(choices=STYLE_CHOICES, max_length=2)
    service = models.CharField(choices=SERVICE_CHOICES, max_length=2)

    def __str__(self):
        """Print function displays username."""
        return self.user.username

    def __repr__(self):
        """Return returns username."""
        return self.user.username

    @property
    def is_active(self):
        """Return if user is active."""
        return self.user.is_active
