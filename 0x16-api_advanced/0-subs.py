#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the
    number of subscribers for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozzila/5.0"}
    rspns = requests.get(url, headers=headers, allow_redirects=False)
    if rspns.status_code == 404:
        return 0
    return rspns.json().get("data").get("subscribers")
