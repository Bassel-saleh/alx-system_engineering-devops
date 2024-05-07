#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        the number of subscribers or 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "MyRedditScraper/1.0 (Contact: basselh26@gmail.com)"
    }
    rspns = requests.get(url, headers=headers, allow_redirects=False)
    if rspns.status_code == 200:
        return rspns.json().get("data").get("subscribers")
    return 0
