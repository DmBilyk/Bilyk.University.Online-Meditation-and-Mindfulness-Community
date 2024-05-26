import timeit
import unittest

from allauth.socialaccount.models import SocialApp
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.test import RequestFactory
from django.test import TestCase, Client
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By

from .models import Profile


class ProfileCustomizationTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password123')
        self.profile = Profile.objects.create(user=self.user, age=25, country='US', bio='Test bio', level='BEG')

    def test_edit_profile_view_authenticated(self):
        self.client.force_login(self.user)

        url = reverse('edit_profile')
        data = {
            'age': 30,
            'country': 'UK',
            'bio': 'Updated bio',
            'level': 'INT',
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.age, 30)
        self.assertEqual(updated_profile.country, 'UK')
        self.assertEqual(updated_profile.bio, 'Updated bio')
        self.assertEqual(updated_profile.level, 'INT')


class ChromeCompatibilityTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_page_loads(self):
        self.driver.get("https://calm-connections.azurewebsites.net/")

        expected_title = "Calm-Connections"
        self.assertEqual(expected_title, self.driver.title)

        translucent_block = self.driver.find_element(By.CLASS_NAME, "hero")
        main_text = self.driver.find_element(By.CLASS_NAME, "hero-text")

        self.assertTrue(translucent_block.is_displayed())
        self.assertTrue(main_text.is_displayed())

    def tearDown(self):
        self.driver.quit()


class TestHomeViewPerformance(TestCase):
    def setUp(self):
        self.client = Client()

        self.social_app = SocialApp.objects.create(
            provider='google',
            name='google',
            client_id='test',
            secret='test',
        )
        self.social_app.sites.add(Site.objects.get_current())

    def test_home_view_performance(self):
        start_time = timeit.default_timer()
        response = self.client.get('/')
        end_time = timeit.default_timer()

        execution_time = end_time - start_time
        print(f"Executed the home view in {execution_time} seconds")

        self.assertEqual(response.status_code, 200)

    class TestFaqViewPerformance(TestCase):
        def setUp(self):
            self.client = Client()

        def test_faq_view_performance(self):
            start_time = timeit.default_timer()
            response = self.client.get('/faq/')
            end_time = timeit.default_timer()

            execution_time = end_time - start_time
            print(f"Executed the faq view in {execution_time} seconds")

            self.assertEqual(response.status_code, 200)


class TestFaqViewPerformance(TestCase):
    def setUp(self):
        self.client = Client()

    def test_faq_view_performance(self):
        start_time = timeit.default_timer()
        response = self.client.get('/faq/')
        end_time = timeit.default_timer()

        execution_time = end_time - start_time
        print(f"Executed the faq view in {execution_time} seconds")

        self.assertEqual(response.status_code, 200)


class TestProfileViewPerformance(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.profile = Profile.objects.create(user=self.user, age=25, country='US', bio='Test bio', level='BEG')

    def test_profile_view_performance(self):
        self.client.login(username='testuser', password='testpass')

        start_time = timeit.default_timer()
        response = self.client.get('/profile/')
        end_time = timeit.default_timer()

        execution_time = end_time - start_time
        print(f"Executed the profile view in {execution_time} seconds")

        self.assertEqual(response.status_code, 200)
