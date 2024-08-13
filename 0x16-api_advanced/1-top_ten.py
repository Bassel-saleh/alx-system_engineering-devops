#!/usr/bin/python3
"""
Script  to print hot posts on a given Reddit subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the 10 hottest posts on a given subreddit

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        titles of the first 10 hot posts listed for the given subreddit or 0
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    rspns = requests.get(url, headers=headers, params=params,
                         allow_redirects=False)
    if rspns.status_code == 404:
        print("None")
        return
    result = rspns.json().get("data")
    [print(c.get("data").get("title")) for c in result.get("children")]
