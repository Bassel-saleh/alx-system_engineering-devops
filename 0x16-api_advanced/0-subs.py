#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "MyRedditScraper/1.0 (Contact: basselh26@gmail.com)"
    }
    rspns = requests.get(url, headers=headers, allow_redirects=False)
    if 'Search results' in rspns.text:
        return 0
    if rspns.status_code != 200:
        return 0
    try:
        result = rspns.json().get("data")
    except json.JSONDecodeError:
        return 0

    return result.get("subscribers", 0)
