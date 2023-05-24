#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_endPoint = "{}/users/{}".format(url, user_id)
    print(user_endPoint)
    user_name = requests.get(user_endPoint).json().get("name")
    print(user_name)

    tasks_endPoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endPoint).json()
    user_tasks = [d for d in tasks if d.get("userId") == user_id]
    tasks_completed = [d for d in user_tasks if d.get("completed")]
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, len(tasks_completed), len(user_tasks)))

    for task in tasks_completed:
        print("\t {}".format(task.get("title")))
