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
        link = 'http://reddit.com/r/{}/hot/.json?'.format(subreddit)
        param = {'count': 10}
        resp = requests.get(link, params=param)
        data = resp.json()
        childparent = data.get('data')
        count = 0
        if childparent is not None and 'children' in childparent:
            children = childparent.get('children')
            for child in children:
                count = count + 1
                print(child.get('data').get('title'))
                if count == 10:
                    return
            return
        print('None')
    except BaseException:
        print('None')
