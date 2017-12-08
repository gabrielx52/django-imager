"""Imager images app urls."""
from django.conf.urls import url

from imager_images.views import (AlbumView, LibraryView, NewAlbumView,
                                 NewPhotoView, PhotoView)

urlpatterns = [
    url(r'^library/$', LibraryView.as_view(),
        name='library'),
    url(r'^albums/(?P<pk>\d+)/$', AlbumView.as_view(), name='album'),
    url(r'^photos/(?P<pk>\d+)/$', PhotoView.as_view(), name='photo'),
    url(r'^albums/add/$', NewAlbumView.as_view(), name='album_form'),
    url(r'^photos/add/$', NewPhotoView.as_view(), name='photo_form'),
]
