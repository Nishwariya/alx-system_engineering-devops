#!/usr/bin/python3
"""Function to count all hot posts on a sub"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns hot posts in a sub"""
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16.api:v1.0.0 (by /u/Pretty_Emmu9894)"
        }
    options = {
        "after": after,
        "count": count,
        "limit": 100
        }
    r = requests.get(link, headers=headers, params=options,
                     allow_redirects=False)
    if r.status_code == 404:
        return None

    results = r.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for s in results.get("children"):
        hot_list.append(s.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
