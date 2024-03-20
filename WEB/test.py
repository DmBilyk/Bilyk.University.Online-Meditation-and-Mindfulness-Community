from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class GoogleAuthTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

    def test_google_auth_redirect(self):

        client = Client()

        response = client.get(reverse('google-auth'))

        self.assertEqual(response.status_code, 302)