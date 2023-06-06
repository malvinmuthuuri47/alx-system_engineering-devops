#!/usr/bin/python3
"""
A module that queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    This function implements the method for querying the API
    and prints the titles of the first 10 hot posts listed
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Edg/113.0.1774.57"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    if response.status_code == 200:
        children = data.get('data').get('children')
        for child in children:
            title = child.get('data').get('title')
            if title is not None:
                print (title)
    else:
        print(None)

