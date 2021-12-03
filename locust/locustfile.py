from locust import HttpUser, task
from locust.user.wait_time import constant_throughput
from random import randint

TASKS_RUN_PER_SECOND = 0.1
LOCALHOST = "http://satiros:8080"


class Client_90_10(HttpUser):
    """
    A simply client that executes GET and ADD tasks, with an execution 
    ratio of 9/1, respectively. That means that the GET task is 9 times 
    more likely of being picked over the ADD task.
    """
    wait_time = constant_throughput(TASKS_RUN_PER_SECOND)
    host = LOCALHOST

    @task(9)
    def get_list(self):
        self.client.get("/get")

    @task
    def add_list(self):
        value = randint(0, 100)
        self.client.post("/add", data=str(value))


class Client_70_30(HttpUser):
    """
    A simply client that executes GET and ADD tasks, with an execution 
    ratio of 7/3, respectively. That means that the GET task is 2.33 times 
    more likely of being picked over the ADD task.
    """
    wait_time = constant_throughput(TASKS_RUN_PER_SECOND)
    host = LOCALHOST

    @task(7)
    def get_list(self):
        self.client.get("/get")

    @task(3)
    def add_list(self):
        value = randint(0, 100)
        self.client.post("/add", data=str(value))


class Client_50_50(HttpUser):
    """
    A simply client that executes GET and ADD tasks, with an
    execution ratio of 5/5, respectively. That means that the
    GET and ADD task have the same chance of being picked.
    """
    wait_time = constant_throughput(TASKS_RUN_PER_SECOND)
    host = LOCALHOST

    @task(5)
    def get_list(self):
        self.client.get("/get")

    @task(5)
    def add_list(self):
        value = randint(0, 100)
        self.client.post("/add", data=str(value))


class Client_30_70(HttpUser):
    """
    A simply client that executes GET and ADD tasks, with an execution 
    ratio of 3/7, respectively. That means that the GET task is 0.43 times 
    more likely of being picked over the ADD task.
    """
    wait_time = constant_throughput(TASKS_RUN_PER_SECOND)
    host = LOCALHOST

    @task(3)
    def get_list(self):
        self.client.get("/get")

    @task(7)
    def add_list(self):
        value = randint(0, 100)
        self.client.post("/add", data=str(value))


class Client_10_90(HttpUser):
    """
    A simply client that executes GET and ADD tasks, with an execution 
    ratio of 1/9, respectively. That means that the GET task is 0.11 times 
    more likely of being picked over the ADD task.
    """
    wait_time = constant_throughput(TASKS_RUN_PER_SECOND)
    host = LOCALHOST

    @task
    def get_list(self):
        self.client.get("/get")

    @task(9)
    def add_list(self):
        value = randint(0, 100)
        self.client.post("/add", data=str(value))
