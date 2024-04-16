from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def load_homepage(self):
        self.client.get("https://calm-connections.azurewebsites.net/")

