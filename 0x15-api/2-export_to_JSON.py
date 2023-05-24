#!/usr/bin/python3
"""Export to Json"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_endPoint = "{}/users/{}".format(url, user_id)
    user_name = requests.get(user_endPoint).json().get("username")

    tasks_endPoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endPoint).json()
    user_tasks = [[user_id, user_name, task.get("completed"),
                  task.get("title")]
                  for task in tasks if user_id == task.get("userId")]

    with open("{}.csv".format(user_id), "w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, quotechar='"')

        for row in user_tasks:
            writer.writerow(row)
