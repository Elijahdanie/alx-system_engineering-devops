#!/usr/bin/python3

"""
This queries the reddit API
and returns the title of
the first 10 hot post
"""

import requests


def top_ten(subreddit):
    """
    This returns the title of the first
    10 hot post on the subreddit
    """
    try:
        link = 'http://reddit.com/r/{}/hot/.json?count=10'.format(subreddit)
        resp = requests.get(link)
        data = resp.json()
        childparent = data.get('data')
        if childparent is not None and 'children' in childparent:
            children = childparent.get('children')
            for child in children:
                print(child['data']['title'])
                return
        print('None')
    except BaseException:
        print('None')
