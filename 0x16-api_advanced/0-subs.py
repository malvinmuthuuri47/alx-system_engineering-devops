#!/usr/bin/python3
"""
A module that queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function implements the method for querying the API
    and returns the total number fo subscribers for a given
    subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Edg/113.0.1774.57"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    if response.status_code == 200:
        count = data.get('data').get('subscribers')
        return count
    return 0
