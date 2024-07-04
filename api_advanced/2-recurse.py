#!/usr/bin/python3

"""
This module defines a recursive function
that fetch the titles of all hot articles
from a given subreddit using the Reddit API.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        # Check if the subreddit exists
        if response.status_code == 404:
            return None

        # Check for valid response
        if response.status_code != 200:
            return None

        data = response.json().get('data', {})

        # Extract titles
        children = data.get('children', [])
        for child in children:
            hot_list.append(child['data']['title'])

        # Check if there is a next page
        after = data.get('after', None)
        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list

    except Exception as e:
        return None
