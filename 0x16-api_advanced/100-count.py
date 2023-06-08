#!/usr/bin/python3
"""This module queries the Reddit API"""
import requests


def count_words(subreddit, word_list, kwargs={}, after=None):
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
            parse_list = child.get("data").get("title").lower().split()
            for element in parse_list:
                if element in word_list:
                    if element in kwargs:
                        kwargs[element] += 1
                    else:
                        kwargs[element] = 1

        if after:
            count_words(subreddit, word_list, kwargs, after)
        else:
            sorted_dict = {k: v for k,
                           v in sorted(kwargs.items(),
                                       key=lambda item: item[1])}
            [print("{}: {}".format(k, v)) for k, v in sorted_dict.items()]
    else:
        return (None)
