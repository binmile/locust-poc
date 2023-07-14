from os import name
from src.helper.utilities import get_random_number_with_N_digit
from locust import SequentialTaskSet, task

import logging


class UserTransaction(SequentialTaskSet):

    @task(3)
    def userLoading(self):
        res1 = self.client.get(f"/api/users?page=2" , name='USER-Task-API1-getusers')
        assert res1.status_code == 200, logging.info(f'[Assertion Failed] get users  API failed for {self.user.demoUser["id"]}  with Response :  {res1.json()} and Response Code : {res1.status_code}')
        userid = res1.json()["data"][0]["id"]
        
        res2 = self.client.get(f"/api/users/{userid}" , name="USER-Task-API2-getuser/id")
        if res2.status_code != 200:
            logging.info(f"get signle user API failed with status code : {res2.status_code} for {self.user.demoUser['id']}")

        res3 = self.client.get(f"/api/users/23" , name="USER-Task-API3-getuser/not-found")
        if res3.status_code != 200:
            logging.info(f"get signle user API failed with status code : {res3.status_code} for {self.user.demoUser['id']}")
    
    @task(1)
    def resourceLoading(self):
        res1 = self.client.get(f"/api/unknown" , name='Resource-API1-getresources')
        assert res1.status_code == 200, logging.info(f'[Assertion Failed] get resources  API failed for {self.user.demoUser["id"]}  with Response :  {res1.json()} and Response Code : {res1.status_code}')
        resid = res1.json()["data"][0]["id"]
        
        res2 = self.client.get(f"/api/unknown/{resid}" , name="Resource-API2-getresources/id")
        assert res2.status_code == 200, logging.info(f"[Assertion Failed] get single resource API failed with status code : {res2.status_code} for {self.user.demoUser['id']}")
        
    @task(1)
    def slowPerformanceLoading(self):
        delayinseconds = get_random_number_with_N_digit(1)
        res1 = self.client.get(f"/api/users?delay={delayinseconds}" , name='Slow-Task-API1-getUsers')
        assert res1.status_code == 200, logging.info(f'[Assertion Failed] slow get resources  API failed for {self.user.demoUser["id"]}  with Response :  {res1.json()} and Response Code : {res1.status_code}')
