from django.test import TestCase, Client
import timeit


class TestHomeViewPerformance(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view_performance(self):
        start_time = timeit.default_timer()
        response = self.client.get('/')
        end_time = timeit.default_timer()

        execution_time = end_time - start_time
        print(f"Executed the home view in {execution_time} seconds")

        self.assertEqual(response.status_code, 200)
