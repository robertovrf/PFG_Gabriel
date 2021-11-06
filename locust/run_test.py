import sys
import os

# Number of users to spawn at peak concurrency
NUMBER_OF_USERS = 100
# Number of users to start per second
SPAWN_RATE = 10
# Run time for the test (Locust will shutdown once the time is up)
RUN_TIME = "180s"
# Time to wait, in seconds, to tasks to finish their iteration
STOP_TIMEOUT = 10


def execute():
    if len(sys.argv) != 2:
        print(f"Especifique o cliente a ser executado...")
        return
    client = sys.argv[1]
    clients = [
        "Client_90_10",
        "Client_70_30",
        "Client_50_50",
        "Client_30_70",
        "Client_10_90",
    ]
    if not client in clients:
        print(f"Cliente invalido...")
        return
    params = {
        "client": client,
        "n_users": NUMBER_OF_USERS,
        "rate":  SPAWN_RATE,
        "time": RUN_TIME,
        "timeout": STOP_TIMEOUT
    }
    cmd = ("locust {client} "
           # run without web UI
           "--headless "
           "-u {n_users} "
           "-r {rate} "
           "--run-time {time} "
           "--stop-timeout {timeout} "
           # stats csv filename's prefix
           "--csv=test "
           # a row for each stats entry is appended every time
           # the stats are written (once every 2 seconds by default)
           "--csv-full-history").format(**params)
    os.system(cmd)


if __name__ == "__main__":
    execute()
