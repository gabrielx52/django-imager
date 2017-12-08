"""Test module for imager profile app."""
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile as Sup
from django.test import Client, TestCase
from django.core.files import File

import factory

from imager_images.models import Album, Photo
from imager_images.forms import NewAlbumForm, NewPhotoForm


from imager_profile.models import ImagerProfile, User


class PhotoFactory(factory.django.DjangoModelFactory):
    """Photo factory to make photos."""

    class Meta:
        """Meta class."""

        model = Photo

    title = factory.Sequence(lambda n: f'Photo{n}')


class PhotoTestCase(TestCase):
    """Photo test case."""

    def setUp(self):
        """Setup."""
        settings.MEDIA_ROOT = tempfile.mkdtemp()
        self.c = Client()

        jimbo = User(username='Jimbo')
        jimbo.set_password('p@ssw0rd')
        jimbo.save()
        jimbo.profile.location = "Buffalo"
        jimbo.profile.save()
        album = Album(user=jimbo.profile, title='The Album')
        album.cover = Sup(name='this_is_fine.png',
                          content=open('media/images/this_is_fine.png',
                                       'rb').read(),
                          content_type='image/png')
        album.save()
        for i in range(30):
            photo = Photo(user=jimbo.profile, title=f'Pic{i}')
            photo.image = Sup(name='this_is_fine.png',
                              content=open('media/images/this_is_fine.png',
                                           'rb').read(),
                              content_type='image/png')
            photo.save()
            album.photo.add(photo)
        self.user = jimbo
        self.album = album

    def test_user_has_30_photos(self):
        """Test that user Jimbo has 30 photo."""
        one_user = User.objects.first()
        self.assertEqual(one_user.profile.photo.count(), 30)

    def test_first_photo_title_is_pic0(self):
        """Test that user Jimbo has 30 photo."""
        one_user = User.objects.first()
        pic = one_user.profile.photo.first()
        self.assertEqual(pic.title, 'Pic0')

    def test_album_created(self):
        """Test that the album is created."""
        one_album = Album.objects.get()
        self.assertIsNotNone(one_album)

    def test_album_title_is_the_album(self):
        """Test that the album title is The Album."""
        one_album = Album.objects.get()
        self.assertEqual(one_album.title, 'The Album')

    def test_album_has_30_photos(self):
        """Test album has 30 photos."""
        one_album = Album.objects.get()
        self.assertEqual(one_album.photo.count(), 30)

    def test_library_view_template_is_library(self):
        """Test library view template is library.html."""
        self.c.login(username='Jimbo', password='p@ssw0rd')
        response = self.c.get('/images/library/')
        self.assertTemplateUsed(response, 'imager_images/library.html')

    def test_library_view_inherits_base_template(self):
        """Test library view inherits base.html template."""
        self.c.login(username='Jimbo', password='p@ssw0rd')
        response = self.c.get('/images/library/')
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_photo_view_template_is_photo(self):
        """Test photo view template is photo.html."""
        pid = Photo.objects.first().id
        response = self.c.get(f'/images/photos/{pid}/')
        self.assertTemplateUsed(response, 'imager_images/photo.html')

    def test_photo_view_inherits_base_template(self):
        """Test photo view inherits base.html template."""
        pid = Photo.objects.first().id
        response = self.c.get(f'/images/photos/{pid}/')
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_album_view_template_is_album(self):
        """Test album view template is album.html."""
        aid = Album.objects.first().id
        response = self.c.get(f'/images/albums/{aid}/')
        self.assertTemplateUsed(response, 'imager_images/album.html')

    def test_album_view_inherits_base_template(self):
        """Test album view inherits base.html template."""
        aid = Album.objects.first().id
        response = self.c.get(f'/images/albums/{aid}/')
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_album_view_status_code_200(self):
        """Test album view has 200 status."""
        aid = Album.objects.first().id
        response = self.c.get(f'/images/albums/{aid}/')
        self.assertEqual(response.status_code, 200)

    def test_photo_view_status_code_200(self):
        """Test photo view has 200 status."""
        pid = Photo.objects.first().id
        response = self.c.get(f'/images/photos/{pid}/')
        self.assertEqual(response.status_code, 200)

    def test_library_view_status_code_200(self):
        """Test library view has 200 status."""
        self.c.login(username='Jimbo', password='p@ssw0rd')
        response = self.c.get('/images/library/')
        self.assertEqual(response.status_code, 200)

    def test_add_photo_view_status_code_302_if_not_logged_in(self):
        """Test add photo view redirects if not logged in."""
        response = self.c.get('/images/photos/add/')
        self.assertEqual(response.status_code, 302)

    def test_add_album_view_status_code_302_if_not_logged_in(self):
        """Test add album view redirects if not logged in."""
        response = self.c.get('/images/albums/add/')
        self.assertEqual(response.status_code, 302)

    def test_add_album_view_template_is_album_form(self):
        """Test add album view template is album_form.html."""
        self.c.login(username='Jimbo', password='p@ssw0rd')
        response = self.c.get(f'/images/albums/add/')
        self.assertTemplateUsed(response, 'imager_images/album_form.html')

    def test_add_photo_view_template_is_photo_form(self):
        """Test add photo view template is photo_view.html."""
        self.c.login(username='Jimbo', password='p@ssw0rd')
        response = self.c.get(f'/images/photos/add/')
        self.assertTemplateUsed(response, 'imager_images/photo_form.html')

    def test_new_album_form_vaild_data(self):
        """Test NewAlbumForm with valid data."""
        photo = [Photo.objects.first().id]
        cover = Sup(name='this_is_fine.png',
                    content=open('media/images/this_is_fine.png',
                                 'rb').read(),
                    content_type='image/png')
        form = NewAlbumForm({'title': 'Test',
                             'description': 'TestDes',
                             'published': 'PBLC',
                             'photo': photo,
                             'cover': cover})
        self.assertTrue(form.is_valid())
