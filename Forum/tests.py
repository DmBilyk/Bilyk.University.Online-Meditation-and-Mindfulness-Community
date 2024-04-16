import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from .views import create_post
from .forms import PostForm
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
