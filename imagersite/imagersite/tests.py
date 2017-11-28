"""Test module for imagersite."""
from bs4 import BeautifulSoup as Soup

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse_lazy


class ViewTestCase(TestCase):
    """View test case."""

    def setUp(self):
        """Client setup."""
        self.c = Client()

        self.bad_user = {'username': 'Andrew',
                         'password': 'f@kenew5'}

        user = User(username='Jane')
        user.set_password('p@ssw0rd')
        user.save()
        self.good_user = {'username': 'Jane',
                          'password': 'p@ssw0rd'}

    def test_home_view_status_code_200(self):
        """Test main view has 200 status."""
        response = self.c.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_has_h1(self):
        """Test home page has h1 div with correct text."""
        response = self.c.get(reverse_lazy('home'))
        self.assertContains(response, b'Djimager home page.')

    def test_home_view_template_is_home(self):
        """Test home view template is home.html."""
        response = self.c.get(reverse_lazy('home'))
        self.assertTemplateUsed(response, 'imagersite/home.html')

    def test_home_view_inherits_base_template(self):
        """Test home view inherits base.html template."""
        response = self.c.get(reverse_lazy('home'))
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_home_view_has_login_link(self):
        """Test home view has login link."""
        response = self.c.get(reverse_lazy('home'))
        soup = Soup(response.content, 'html.parser')
        self.assertIsNotNone(soup.find('a', {'href': '/login/'}))

    def test_login_view_status_code_200(self):
        """Test login view has 200 status."""
        response = self.c.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_bad_user_goes_back_to_login(self):
        """Test login with unregistered user goes back to login page."""
        response = self.c.post(reverse_lazy('login'), self.bad_user)
        self.assertTemplateUsed(response, 'imagersite/login.html')

    def test_login_with_bad_user_goes_back_to_login_with_error_text(self):
        """Test bad login has error text."""
        response = self.c.post(reverse_lazy('login'), self.bad_user)
        self.assertContains(response, 'Please enter a', status_code=200)

    def test_login_with_no_password_goes_back_to_login(self):
        """Test login attempt with no password goes back to login."""
        data = {'username': 'bob'}
        response = self.c.post(reverse_lazy('login'), data)
        self.assertTemplateUsed(response, 'imagersite/login.html')

    def test_login_with_no_username_goes_back_to_login(self):
        """Test login attempt with no username goes back to login."""
        data = {'password': 'f@kenew5'}
        response = self.c.post(reverse_lazy('login'), data)
        self.assertTemplateUsed(response, 'imagersite/login.html')

    def test_login_with_valid_user_has_302_status_code(self):
        """Test that successful login will have 302 status code."""
        response = self.c.post(reverse_lazy('login'), self.good_user)
        self.assertEqual(response.status_code, 302)

    def test_login_with_valid_user_redirects_to_home(self):
        """Test that successful login will redirect to home."""
        response = self.c.post(reverse_lazy('login'),
                               self.good_user,
                               follow=True)
        self.assertTemplateUsed(response, 'imagersite/home.html')

    def test_login_with_valid_user_home_displays_name(self):
        """Test that successful login will redirect to home."""
        response = self.c.post(reverse_lazy('login'),
                               self.good_user,
                               follow=True)
        self.assertContains(response, 'Hello Jane', status_code=200)

    def test_logout_view_status_code_302(self):
        """Test logout view has 302 status."""
        response = self.c.get(reverse_lazy('logout'))
        self.assertEqual(response.status_code, 302)

    def test_register_view_status_code_200(self):
        """Test register view has 200 status."""
        response = self.c.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)
