"""Test module for imager profile app."""

from django.test import TestCase

import factory

from imager_images.models import Album, Photo

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
        jimbo = User(username='Jimbo',
                     password='p@ssw0rd')
        jimbo.save()
        j_profile = jimbo.profile
        j_profile.location = "Buffalo"
        j_profile.save()
        # for i in range(30):
        #     self.photo = PhotoFactory.create()
        #     self.photo.user = j_profile
        #     self.photo.save()

    
    def test_user_is_jimbo(self):
        """Test the username is Jimbo."""
        one_user = User.objects.first()
        self.assertEqual(one_user.username, 'Jimbo')

