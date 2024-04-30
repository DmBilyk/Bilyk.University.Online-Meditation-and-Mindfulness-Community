from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
import timeit
from .forms import TaskForm
from .models import Task, TaskCategory


class TaskManagementTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Create a task category
        self.task_category = TaskCategory.objects.create(name='Test Category', description='Test Description',
                                                         color='#003bff')
        # Create a task
        self.task = Task.objects.create(user=self.user, description='Test Task', category=self.task_category)

    def test_calendar_view(self):
        client = Client()
        client.login(username='testuser', password='12345')
        response = client.get(reverse('calendar'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_add_task_view(self):
        client = Client()
        client.login(username='testuser', password='12345')
        response = client.get(reverse('add_task'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], TaskForm)

    def test_complete_task_view(self):
        client = Client()
        client.login(username='testuser', password='12345')
        response = client.post(reverse('complete_task', args=[self.task.id]))
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)
        self.assertEqual(response.status_code, 302)

    def test_delete_task_view(self):
        client = Client()
        client.login(username='testuser', password='12345')
        response = client.post(reverse('delete_task', args=[self.task.id]))
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
        self.assertEqual(response.status_code, 302)


class TestCalendarViewPerformance(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_calendar_view_performance(self):
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        start_time = timeit.default_timer()
        response = self.client.get('/calendar/')
        end_time = timeit.default_timer()

        execution_time = end_time - start_time
        print(f"Executed the calendar view in {execution_time} seconds")

        self.assertEqual(response.status_code, 200)
