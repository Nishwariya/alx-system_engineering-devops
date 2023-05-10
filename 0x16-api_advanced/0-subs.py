#!/usr/bin/python3
"""
A function to query Reddit API and return the number of subs
if an invalid subreddit is given, the function should return
0
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subs in a subreddit"""
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    auth = {
            "User-Agent": "subs:v1.0.0 (by /u/Pretty_Emu9894)"
            }
    response = requests.get(link, headers=auth, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json().get("data")
    return res.get("subscribers")
