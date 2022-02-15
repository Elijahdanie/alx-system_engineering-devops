#!/usr/bin/python3

"""
This fetches the titles of
hot topics on a given subreddit
from the reddit api on all pages
recursively
"""

import requests


def recurse(subreddit, after=None, count=0, hot_list=[]):
    """
    fetches hot topics
    of a subreddit
    """
    next_page = {} if after is None else {'after': after}
    next_page['count'] = count
    header = {'User-Agent': 'elijahdanie'}
    link = 'http://reddit.com/r/{}/hot/.json?'.format(subreddit)
    resp = requests.get(link, params=next_page, headers=header)
    data = resp.json()
    childparent = data.get('data')
    if childparent is not None and 'children' in childparent:
        after = childparent.get('after')
        count = childparent.get('count')
        if after is None:
            return hot_list
        children = childparent.get('children')
        for child in children:
            hot_list.append(child['data']['title'])
        return recurse(subreddit, after, count, hot_list)
