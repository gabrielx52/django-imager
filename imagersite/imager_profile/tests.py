"""Test module for imager profile app."""

from django.test import TestCase

import factory

from imager_profile.models import ImagerProfile, User


class UserFactory(factory.django.DjangoModelFactory):
    """User factory to make users."""

    class Meta:
        """No idea what this is."""

        model = User

    username = factory.Sequence(lambda n: f'Johnny{n}')


class ProfileTestCase(TestCase):
    """Pofile test case."""

    def setUp(self):
        """Setup."""
        for i in range(30):
            self.user = UserFactory.create()
            self.user.save()
            profile = self.user.profile
            profile.location = 'Anywhere but here'
            profile.save()
        unique_user = User(username='Jalen',
                           password='F@kep@ssw0rd')
        unique_user.save()
        profile = unique_user.profile
        profile.location = 'Seattle'
        profile.camera = 'FL'
        profile.service = 'PT'
        profile.photo_style = 'NT'
        profile.save()

    def test_user_can_point_to_profile(self):
        """Test user can point to profile."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)

    def test_set_up_creates_31_users(self):
        """Test setUp creates 30 users."""
        self.assertEqual(User.objects.count(), 31)

    def test_user_is_a_johnny(self):
        """Test the first user is a Johnny."""
        one_user = User.objects.first()
        self.assertTrue(one_user.username.startswith('Johnny'))

    def test_user_has_location_via_profile(self):
        """Test user has a location."""
        one_user = User.objects.first()
        self.assertEqual(one_user.profile.location, 'Anywhere but here')

    def test_user_jalen_has_film_camera(self):
        """Test user Jalen has correct Camera choice."""
        jalen = User.objects.last()
        self.assertEqual(jalen.profile.get_camera_display(), 'Film')

    def test_user_jalen_style_is_nature(self):
        """Test user Jalen's style is Nature."""
        jalen = User.objects.last()
        self.assertEqual(jalen.profile.get_photo_style_display(), 'Nature')

    def test_user_jalen_has_printing_service(self):
        """Test user Jalen's service is Printing."""
        jalen = User.objects.last()
        self.assertEqual(jalen.profile.get_service_display(), 'Printing')

    def test_user_jalen_location_is_seattle(self):
        """Test user Jalen's location is Seattle."""
        jalen = User.objects.last()
        self.assertEqual(jalen.profile.location, 'Seattle')

    def test_str_displays_username(self):
        """Test that username is displayed when using the print function."""
        one_user = User.objects.last()
        self.assertEqual(str(one_user), 'Jalen')

    def test_is_active_property_returns_users_active_state(self):
        """Test is active property returns if user is active."""
        one_user = User.objects.last()
        self.assertTrue(one_user.profile.is_active)

    def test_active_manager_works(self):
        """Test is active manager_works."""
        self.assertEqual(ImagerProfile.active.count(), 31)

    def test_str_attr_displays_username(self):
        """Test that username is displayed when using str attr."""
        one_user = User.objects.last()
        self.assertEqual(one_user.__str__(), 'Jalen')
