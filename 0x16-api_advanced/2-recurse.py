#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit

    Args:
        subreddit: The name of the subreddit
        hot_list: List to store the post titles

    Returns:
        list: A list of post titles from the hot section of the subreddit
        if not valid returns None
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    rspns = requests.get(url, headers=headers, params=params,
                         allow_redirects=False)
    if rspns.status_code == 404:
        return None
    result = rspns.json().get("data")
    after = result.get("after")
    count += result.get("dist")
    for c in result.get("children"):
        hot_list.append(c.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
