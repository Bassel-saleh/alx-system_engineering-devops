#!/usr/bin/python3
import requests
import json


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit

    Args:
        subreddit (str): The name of the subreddit
        hot_list (list, optional): List to store the post titles
                                    Default is an empty list

    Returns:
        list: A list of post titles from the hot section of the subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    rspns = requests.get(url, headers=headers)
    if rspns.status_code != 200:
        return None

    try:
        data = rspns.json().get("data")
    except json.JSONDecodeError:
        return None
    hot_list.extend([post["data"]["title"] for post in data["children"]])
    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list)
    else:
        return hot_list
