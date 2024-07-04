#!/usr/bin/python3
"""
This module defines a recursive function to fetch the titles of all hot articles
from a given subreddit using the Reddit API and count the occurrences of specified
keywords in those titles. The results are printed in descending order by count,
and if counts are the same, they are sorted alphabetically.
"""

import requests
from collections import Counter
import re


def count_words(subreddit, word_list, hot_list=[], after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    """
    if word_count is None:
        word_count = Counter()

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the subreddit exists
        if response.status_code == 404:
            return

        # Check for valid response
        if response.status_code != 200:
            return

        data = response.json().get('data', {})

        # Extract titles
        children = data.get('children', [])
        for child in children:
            hot_list.append(child['data']['title'])

        # Check if there is a next page
        after = data.get('after', None)
        if after:
            return count_words(subreddit, word_list, hot_list, after, word_count)

        # Count keywords in titles
        word_list = [word.lower() for word in word_list]
        for title in hot_list:
            title_words = re.findall(r'\b\w+\b', title.lower())
            for word in word_list:
                word_count[word] += title_words.count(word)

        # Filter out words with zero counts
        word_count = {word: count for word, count in word_count.items() if count > 0}

        # Sort results by count (descending) and alphabetically (ascending)
        sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

        # Print results
        for word, count in sorted_word_count:
            print("{}: {}".format(word, count))

    except Exception as e:
        return
