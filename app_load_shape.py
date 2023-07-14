import logging
import math
import requests
from locust import HttpUser, LoadTestShape, between, events
from locust.user.task import TaskSet, task

from src.helper.user_setup import UserSetup
from src.tests.user_transaction import UserTransaction


class DemoLoadTest(HttpUser):
    host = "https://reqres.in"
    tasks = [UserTransaction]
    connection_timeout = 120.0
    network_timeout = 120.0
    wait_time = between(1, 5)
    USER_IDS = []

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        logging.info("started load test")
        
    def on_start(self):
        UserSetup.user_login(self)

class StageShape(LoadTestShape):
    stages = [
        {"duration": 10, "users": 5, "spawn_rate": 5},
        {"duration": 30, "users": 15, "spawn_rate": 5},
        {"duration": 60, "users": 30, "spawn_rate": 10},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None