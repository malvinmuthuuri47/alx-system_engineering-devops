#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_endPoint = "{}/users".format(url)
    users = requests.get(user_endPoint).json()

    tasks_endPoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endPoint).json()

    user_tasks = {
            user.get("id"): [
                {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                for task in tasks if task.get("userId") == user.get("id")
            ]
            for user in users
    }

    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        json.dump(user_tasks, file)
