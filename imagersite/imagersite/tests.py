"""Test module for imagersite."""
from bs4 import BeautifulSoup as Soup

from django.contrib.auth.models import User
from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse_lazy


class ViewTestCase(TestCase):
    """View test case."""

    def setUp(self):
        """Client setup."""
        self.c = Client()

        self.bad_user = {'username': 'Allan',
                         'password': 'm@ttshouldquit'}

        user = User(username='Jane')
        user.set_password('p@ssw0rd')
        user.save()
        self.good_user = {'username': 'Jane',
                          'password': 'p@ssw0rd'}

        self.reg_data = {'username': 'Joel',
                         'password1': 'Thep@ssw0rd',
                         'password2': 'Thep@ssw0rd',
                         'email': 'Joel@juno.com'}

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

    def test_login_logout_home_display_has_no_name(self):
        """Test that home will not display name after login and logout."""
        response = self.c.post(reverse_lazy('login'),
                               self.good_user,
                               follow=True)
        self.assertContains(response, 'Hello Jane', status_code=200)
        response = self.c.get(reverse_lazy('logout'), follow=True)
        self.assertNotContains(response, 'Hello Jane', status_code=200)

    def test_logout_view_status_code_302(self):
        """Test logout view has 302 status."""
        response = self.c.get(reverse_lazy('logout'))
        self.assertEqual(response.status_code, 302)

    def test_register_view_status_code_200(self):
        """Test register view has 200 status."""
        response = self.c.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_register_status_code_302_after_registration(self):
        """Test register has 302 code after registration."""
        response = self.c.post(reverse_lazy('registration_register'),
                               self.reg_data)
        self.assertEqual(response.status_code, 302)

    def test_register_redirects_to_registration_complete(self):
        """Test register redirects to registration complete page."""
        response = self.c.post(reverse_lazy('registration_register'),
                               self.reg_data,
                               follow=True)
        self.assertTemplateUsed(response,
                                'registration/registration_complete.html')

    def test_register_sends_email(self):
        """Test register sends email."""
        self.c.post(reverse_lazy('registration_register'),
                    self.reg_data,
                    follow=True)
        self.assertEqual(len(mail.outbox), 1)

    def test_register_email_has_subject(self):
        """Test register email has correct subject."""
        self.c.post(reverse_lazy('registration_register'),
                    self.reg_data,
                    follow=True)
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Djimager registration email.')

    def test_register_email_link_acctivates_account(self):
        """Test register email has correct subject."""
        self.c.post(reverse_lazy('registration_register'),
                    self.reg_data,
                    follow=True)
        content = mail.outbox[0].message().get_payload()
        link = content.split('\n\n')[2]
        self.c.get(link)
        user = User.objects.get(username='Joel')
        self.assertTrue(user.is_active)
