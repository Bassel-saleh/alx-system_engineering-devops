#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit
"""
import json
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit currently

    Args:
        subreddit (str): The name of the subreddit
        hot_list (list, optional): List to store the post titles
                                    Default is an empty list
        after (str, optional): Token used for pagination
                                Default is an empty string
        count (int, optional): Current count of retrieved posts. Default is 0

    Returns:
        list: A list of post titles from the hot section of the subreddit
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
    if rspns.status_code != 200:
        return None
    try:
        result = rspns.json().get("data")
    except json.JSONDecodeError:
        return None
    if not result or not result.get("children"):
        return None
    after = result.get("after")
    count += result.get("dist")
    for c in result.get("children"):
        hot_list.append(c.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
