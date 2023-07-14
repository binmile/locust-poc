import logging, pathlib
import time

from src.helper.utilities import *

class UserSetup():
    def user_login(self):
        self.demoUser = {}
        self.client.headers = {}
        # adding 16 digit guid as X-DEVICE-ID header for all request
        self.client.headers['X-DEVICE-ID'] = getUUID(16)
        # adding language header as English
        self.client.headers['Accept-Language'] = 'EN'
        self.client.headers['Content-Type'] = 'application/json'

        self.demoUser['id'] = get_random_number_with_N_digit(16)

        # user do login
        body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        res = self.client.post(f"/api/login", json = body, name="1-UserSetup-API1-login")
        assert res.status_code == 200, logging.info(f'[Assertion Failed] login  API failed for {self.demoUser["id"]}  with Response :  {res.json()} and Response Code : {res.status_code}')
        self.client.headers['Authorization'] = res.json()["token"]
        

       