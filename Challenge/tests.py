from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import WeeklyChallenge, UserChallenge, DayTask
from django.utils import timezone
from datetime import timedelta


class ChallengeTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.challenge = WeeklyChallenge.objects.create(
            title='Test Challenge',
            end_date=timezone.now() + timedelta(days=7)  # for example, one week from now
        )
        self.day_task = DayTask.objects.create(title='Test Task', description='Test Description', day_number=1)
        self.challenge.tasks.add(self.day_task)

    def test_challenge_list(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/challenges/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Challenge')

    def test_join_challenge(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(f'/challenges/join/{self.challenge.id}/')
        self.assertEqual(response.status_code, 302)
        user_challenge = UserChallenge.objects.get(user=self.user, challenge=self.challenge)
        self.assertTrue(user_challenge.is_joined)

    def test_challenge_detail(self):
        self.client.login(username='testuser', password='12345')
        UserChallenge.objects.create(user=self.user, challenge=self.challenge, is_joined=True)
        response = self.client.get(f'/challenges/{self.challenge.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Challenge')
        self.assertContains(response, 'Test Task')
