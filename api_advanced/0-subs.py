#!/usr/bin/python3

"""Importing request library to get data from Url"""
import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers function
    that get date from reddit
    and returns number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)
    data = response.json()
    return data['data']['subscribers']
