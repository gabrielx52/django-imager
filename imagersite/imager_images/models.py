"""Imager images app models."""
from django.db import models

from imager_profile.models import ImagerProfile


class Photo(models.Model):
    """Photo model."""

    PUBLISHED = (('PRVT', 'private'),
                 ('SHRD', 'shared'),
                 ('PBLC', 'public'))
    image = models.ImageField(upload_to='images')
    user = models.ForeignKey(ImagerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=500, blank=True, null=True)
    date_uploaded = models.DateField(editable=False, auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(choices=PUBLISHED, max_length=8)


class Album(models.Model):
    """Album model."""

    PUBLISHED = (('PRVT', 'private'),
                 ('SHRD', 'shared'),
                 ('PBLC', 'public'))
    user = models.ForeignKey(ImagerProfile, on_delete=models.CASCADE)
    photo = models.ManyToManyField(Photo, related_name='album')
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=500, blank=True, null=True)
    cover = models.ImageField(upload_to='images')
    date_created = models.DateField(editable=False, auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(choices=PUBLISHED, max_length=8)
