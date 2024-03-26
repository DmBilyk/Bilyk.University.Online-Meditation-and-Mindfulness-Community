from django.test import TransactionTestCase
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialApp


class GoogleRegistrationTest(TransactionTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')

    def test_google_registration(self):
        # Створення фейкового об'єкта SocialApp для провайдера Google
        google_app = SocialApp.objects.create(provider='google',
                                              name='Calm-Connections',
                                              client_id='your_google_client_id',
                                              secret='your_google_client_secret')

        # Виконання запиту до /google/login/callback/?code=valid-google-token
        response = self.client.get('/google/login/callback/?code=valid-google-token')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertTrue(self.user.socialaccount_set.filter(provider='google').exists())

        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(response, '/home/')
