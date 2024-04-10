from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def load_homepage(self):
        self.client.get("https://calm-connections.azurewebsites.net/")

# class FeedbackFormUser(HttpUser):
#     wait_time = between(5, 15)
#
#     @task
#     def submit_feedback(self):
#         # Prepare data for feedback form submission
#         data = {
#             'customer_name': 'Test Customer',
#             'email': 'test@example.com',
#             'product': 'Test Product',
#             'details': 'Test details',
#             'happy': True,
#         }
#
#
#         response = self.client.post('/feedback_form/', data=data)
#
#
#         assert response.status_code == 200
#
#     def on_stop(self):
#         pass
