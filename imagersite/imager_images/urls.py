"""Imager images app urls."""
from django.conf.urls import url

from imager_images.views import (AlbumUpdate, AlbumView, LibraryView,
                                 NewAlbumView, NewPhotoView, PhotoUpdate,
                                 PhotoView)

urlpatterns = [
    url(r'^library/$', LibraryView.as_view(),
        name='library'),
    url(r'^albums/(?P<pk>\d+)/$', AlbumView.as_view(), name='album'),
    url(r'^photos/(?P<pk>\d+)/$', PhotoView.as_view(), name='photo'),
    url(r'^albums/add/$', NewAlbumView.as_view(), name='album_form'),
    url(r'^photos/add/$', NewPhotoView.as_view(), name='photo_form'),
    url(r'^albums/(?P<pk>\d+)/edit/$', AlbumUpdate.as_view(),
        name='album_update'),
    url(r'^photos/(?P<pk>\d+)/edit/$', PhotoUpdate.as_view(),
        name='photo_update'),
]
