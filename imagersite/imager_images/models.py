"""Imager images app models."""
from django.db import models

from imager_profile.models import ImagerProfile


class ImageBaseClass(models.Model):
    """Base class for Photo and Album classes."""

    PRIVATE = 'PRVT'
    SHARED = 'SHRD'
    PUBLIC = 'PBLC'

    PUBLISHED = ((PRIVATE, 'private'),
                 (SHARED, 'shared'),
                 (PUBLIC, 'public'))
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=500, blank=True, null=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(choices=PUBLISHED, max_length=8)

    class Meta:
        """Meta."""

        abstract = True


class Photo(ImageBaseClass):
    """Photo model."""

    user = models.ForeignKey(ImagerProfile, on_delete=models.CASCADE,
                             related_name='photo')
    image = models.ImageField(upload_to='images')
    date_uploaded = models.DateField(editable=False, auto_now_add=True)

    def __str__(self):
        """Print function displays username."""
        return self.title


class Album(ImageBaseClass):
    """Album model."""

    user = models.ForeignKey(ImagerProfile, on_delete=models.CASCADE,
                             related_name='album')
    photo = models.ManyToManyField(Photo, related_name='album')
    cover = models.ImageField(upload_to='images', blank=True, null=True)
    date_created = models.DateField(editable=False, auto_now_add=True)

    def __str__(self):
        """Print function displays username."""
        return self.title
