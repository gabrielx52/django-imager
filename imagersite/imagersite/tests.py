"""Test module for imagersite."""
from django.test import Client, TestCase


class ViewTestCase(TestCase):
    """View test case."""

    def test_main_view_status_code_200(self):
        """Test main view has 200 status."""
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_view_status_code_200(self):
        """Test login view has 200 status."""
        c = Client()
        response = c.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout_view_status_code_302(self):
        """Test logout view has 302 status."""
        c = Client()
        response = c.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_register_view_status_code_200(self):
        """Test register view has 200 status."""
        c = Client()
        response = c.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
