#!/usr/bin/python3
"""This module queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    This function implements recursion where you query an API for a
    given subreddit so long as the subreddit is valid, otherwise return None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "Edg/113.0.1774.57"}

    params = {"after": after}

    data = requests.get(url, headers=headers, allow_redirects=False,
                        params=params)

    if data.status_code == 200:
        after = data.json().get("data").get("after")
        children = data.json().get("data").get("children")
        for child in children:
            hot_list.append(child.get("data").get("title"))

        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
