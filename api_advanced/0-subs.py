#!/usr/bin/python3
"""
Importing Required Modules like request.
in order to get number if subscribers of reddit
"""


import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers returns number of subscribers."""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Bot/1.0)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
