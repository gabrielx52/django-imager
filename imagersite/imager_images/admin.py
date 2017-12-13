"""Photo and Album models."""
from django.contrib import admin

from imager_images.models import Album, Photo


admin.site.register(Album)
admin.site.register(Photo)
