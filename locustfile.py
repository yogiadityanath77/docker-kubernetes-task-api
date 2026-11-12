
from locust import HttpUser, task, between
import time


class TaskAPIUser(HttpUser):

    # Wait between 1 and 2 seconds
    # before performing another request
    wait_time = between(1, 2)

    # Health check
    @task(5)
    def health_check(self):
        self.client.get("/health")

    # Fetch all tasks
    @task(3)
    def get_tasks(self):
        self.client.get("/tasks")

    # Create a task
    @task(1)
    def create_task(self):
        self.client.post(
            "/tasks",
            json={
                "title": f"Load Test {time.time_ns()}",
                "completed": False
            }
        )
