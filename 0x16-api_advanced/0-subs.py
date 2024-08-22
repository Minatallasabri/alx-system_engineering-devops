#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url,  headers={"User-Agent": "Custom"})
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data').get('subscribers')
        return subscribers
    else:
        return 0
