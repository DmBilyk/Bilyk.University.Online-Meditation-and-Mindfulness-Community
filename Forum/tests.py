from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post, Response

class ForumTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(user=self.user, message='Test Post')
        self.response = Response.objects.create(parent_post=self.post, message='Test Response')

    def test_forum_index(self):
        response = self.client.get('/forum/')  # Corrected URL
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test Response')

    def test_create_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/forum/create/', {'message': 'New Post'})  # Corrected URL
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(message='New Post').exists())

    def test_reply_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(f'/forum/reply/{self.post.id}/', {'message': 'New Response'})  # Corrected URL
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Response.objects.filter(message='New Response').exists())
