from django.test import TestCase
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialApp

class GoogleRegistrationTest(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='secret')

       # elf.google_app = SocialApp.objects.create(provider='Google', name='Calm-Connections', client_id='client_id')

    def test_google_registration(self):

        response = self.client.get('/google/login/callback/?code=valid-google-token')

        self.assertEqual(response.status_code, 200)


        self.assertTrue(User.objects.filter(username='testuser').exists())


        self.assertTrue(self.user.socialaccount_set.filter(provider='Google').exists())


        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(response, '/dashboard/')
