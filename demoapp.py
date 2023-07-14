import logging
from typing_extensions import Self
from locust import HttpUser, SequentialTaskSet, TaskSet, between, task



class UserTransaction(SequentialTaskSet):
    @task()
    def fetchlist(self):
        res1 = self.client.get(f"/api/users?page=2" , name='USER-Task-API1-getusers')
        assert res1.status_code == 200, logging.info(f'[Assertion Failed] get users  API failed for {self.user.demoUser["id"]}  with Response :  {res1.json()} and Response Code : {res1.status_code}')

class userSetup:
    def login(self):    
        # user do login
        body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        res = self.client.post(f"/api/login", json = body, name="1-UserSetup-API1-login")
        assert res.status_code == 200, logging.info(f'[Assertion Failed] login  API failed for {self.demoUser["id"]}  with Response :  {res.json()} and Response Code : {res.status_code}')
        self.client.headers['Authorization'] = res.json()["token"]

class DemoLoadTest(HttpUser):
    host = "https://reqres.in"
    tasks = [UserTransaction]
    wait_time = between(1, 5)

    def on_start(self):
        userSetup.login(self)




        


