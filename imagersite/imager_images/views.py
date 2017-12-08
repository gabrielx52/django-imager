"""Django profile app views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, TemplateView


from imager_images.models import Album, Photo

from imager_profile.models import ImagerProfile


class LibraryView(TemplateView):
    """Library view class based view."""

    template_name = 'imager_images/library.html'

    def get_context_data(self, username=None):
        """Get context data for view."""
        user = User.objects.get(username=self.request.user)
        return {'user': user}


class PhotoView(DetailView):
    """Photo view class based view."""

    template_name = 'imager_images/photo.html'
    model = Photo
    queryset = Photo.objects.all()


class AlbumView(DetailView):
    """Album view class based view."""

    template_name = 'imager_images/album.html'
    model = Album
    queryset = Album.objects.all()


class NewAlbumView(LoginRequiredMixin, CreateView):
    """Album form view."""

    template_name = 'imager_images/album_form.html'
    model = Album
    fields = ['title', 'description', 'published', 'photo', 'cover']
    success_url = '/images/library/'
    redirect_field_name = '/login/'

    def form_valid(self, form):
        """Validate form."""
        form_user = ImagerProfile.objects.get(user=self.request.user)
        form.instance.user = form_user
        return super(NewAlbumView, self).form_valid(form)


class NewPhotoView(LoginRequiredMixin, CreateView):
    """Photo form view."""

    template_name = 'imager_images/photo_form.html'
    model = Photo
    fields = ['title', 'description', 'published', 'image']
    success_url = '/images/library/'
    redirect_field_name = '/login/'

    def form_valid(self, form):
        """Validate form."""
        form_user = ImagerProfile.objects.get(user=self.request.user)
        form.instance.user = form_user
        return super(NewPhotoView, self).form_valid(form)
