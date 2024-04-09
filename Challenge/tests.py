from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from .models import WeeklyChallenge, UserChallenge, DayTask


class ChallengeTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Create a day task
        self.day_task = DayTask.objects.create(title='Test Task', description='Test Description', day_number=1)
        # Create a weekly challenge
        self.weekly_challenge = WeeklyChallenge.objects.create(title='Test Challenge',
                                                               end_date=timezone.now() + timezone.timedelta(days=7))
        self.weekly_challenge.tasks.add(self.day_task)
        # Create a user challenge
        self.user_challenge = UserChallenge.objects.create(user=self.user, challenge=self.weekly_challenge)

    def test_challenge_list_view(self):
        client = Client()
        client.login(username='testuser', password='12345')
        response = client.get(reverse('challenge_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Challenge')

    def test_join_challenge_view(self):
        client = Client()
        client.login(username='testuser', password='12345')
        response = client.get(reverse('join_challenge', args=[self.weekly_challenge.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            UserChallenge.objects.filter(user=self.user, challenge=self.weekly_challenge, is_joined=True).exists())

    def test_challenge_detail_view(self):
        client = Client()
        client.login(username='testuser', password='12345')
        response = client.get(reverse('challenge_detail', args=[self.weekly_challenge.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

# Note: The test cases assume that the views and URL patterns are correctly set up with the names 'challenge_list', 'join_challenge', and 'challenge_detail'.
# The test cases also assume that the templates 'challenges/challenge_list.html' and 'challenges/challenge_detail.html' exist and are correctly set up.
