import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from .views import create_post
from django.test import TestCase, Client
from django.contrib.auth.models import User
import timeit
from .models import Post


@pytest.fixture
def user():
    return User.objects.create_user(username='test', password='test')


@pytest.fixture
def factory():
    return RequestFactory()


def test_create_post_with_valid_data(factory, user):
    request = factory.post('/create_post/', {'message': 'Test message'})
    request.user = user
    response = create_post(request)
    assert response.status_code == 302
    assert Post.objects.count() == 1
    assert Post.objects.first().message == 'Test message'


def test_create_post_with_invalid_data(factory, user):
    request = factory.post('/create_post/', {'message': ''})
    request.user = user
    response = create_post(request)
    assert response.status_code == 200
    assert Post.objects.count() == 0


def test_create_post_with_anonymous_user(factory):
    request = factory.post('/create_post/', {'message': 'Test message'})
    request.user = AnonymousUser()
    response = create_post(request)
    assert response.status_code == 302
    assert Post.objects.count() == 0


def test_create_post_with_parent_post(factory, user):
    parent_post = Post.objects.create(user=user, message='Parent post')
    request = factory.post('/create_post/', {'message': 'Test message', 'parent_post_id': parent_post.id})
    request.user = user
    response = create_post(request)
    assert response.status_code == 302
    assert Post.objects.count() == 2
    assert Post.objects.last().parent_post == parent_post


def test_create_post_with_nonexistent_parent_post(factory, user):
    request = factory.post('/create_post/', {'message': 'Test message', 'parent_post_id': 999})
    request.user = user
    response = create_post(request)
    assert response.status_code == 200
    assert Post.objects.count() == 0


class TestForumViewPerformance(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_forum_view_performance(self):
        self.client.login(username='testuser', password='testpass')

        start_time = timeit.default_timer()
        response = self.client.get('/forum/')
        end_time = timeit.default_timer()

        execution_time = end_time - start_time
        print(f"Executed the forum view in {execution_time} seconds")

        self.assertEqual(response.status_code, 200)
