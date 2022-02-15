#!/usr/bin/python3

"""
This gets the subscribers of
a subreddit
"""

from sys import argv
import sys
import requests


def number_of_subscribers(subreddit):
    """
    Gets number of subscribers of a subreddit
    """
    link = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    resp = requests.get(link)
    data = resp.json()
    if 'data' in data:
        if 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0
