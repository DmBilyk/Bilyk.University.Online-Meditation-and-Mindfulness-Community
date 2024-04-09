from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Response
from .forms import PostForm


class ForumTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Create a post
        self.post = Post.objects.create(user=self.user, message='Test Post')
        # Create a response
        self.response = Response.objects.create(parent_post=self.post, message='Test Response')

    def test_forum_index_view(self):
        client = Client()
        client.login(username='testuser', password='12345')
        response = client.get(reverse('forum_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test Response')

    def test_create_post_view(self):
        client = Client()
        client.login(username='testuser', password='12345')
        response = client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PostForm)

        # Test creating a new post
        response = client.post(reverse('create_post'), {'message': 'New Test Post'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(message='New Test Post').exists())

        # Test creating a response to an existing post
        response = client.post(reverse('create_post') + f'?parent_post_id={self.post.id}',
                               {'message': 'New Test Response'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Response.objects.filter(message='New Test Response', parent_post=self.post).exists())
