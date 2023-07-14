import logging
import requests
from locust import HttpUser, between, events
from src.helper.utilities import get_random_number_with_N_digit, getUUID

from src.helper.user_setup import UserSetup
from src.tests.user_transaction import UserTransaction


class DemoLoadTest(HttpUser):
    host = "https://reqres.in"
    tasks = [UserTransaction]
    connection_timeout = 120.0
    network_timeout = 120.0
    wait_time = between(0, 1)

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        logging.info("started load test")
        
    def on_start(self):
        UserSetup.user_login(self)
