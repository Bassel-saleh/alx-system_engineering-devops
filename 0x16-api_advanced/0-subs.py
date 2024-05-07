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
        hot_list (list, optional): List to store the post titles.
                                    Default is an empty list.
        after (str, optional): Token used for pagination.
                                Default is an empty string.
        count (int, optional): Current count of retrieved posts. Default is 0.

    Returns:
        the number of subscribers or 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    rspns = requests.get(url, headers=headers, allow_redirects=False)
    if rspns.status_code == 200:
        return rspns.json().get("data").get("subscribers")
    return 0
