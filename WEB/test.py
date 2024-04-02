from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



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

        expected_title = "Calm-Connection"
        self.assertEqual(expected_title, self.driver.title)

        translucent_block = self.driver.find_element(By.CLASS_NAME, "translucent-block")
        main_text = self.driver.find_element(By.CLASS_NAME, "main-text")

        self.assertTrue(translucent_block.is_displayed())
        self.assertTrue(main_text.is_displayed())

    def tearDown(self):
        self.driver.quit()
