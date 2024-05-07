#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit
    If an invalid subreddit is given, the function should return 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Custom"
    }
    rspns = requests.get(url, headers=headers, allow_redirects=False)
    if rspns.status_code == 404:
        return 0
    result = rspns.json().get("data")
    return result.get("subscribers")
