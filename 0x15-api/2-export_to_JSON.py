#!/usr/bin/python3

"""
This module gets the todo of a user identified by id
gotten from the api https://jsonplaceholder.typicode.com
"""

import json
import requests
import sys

api_url = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    if len(sys.argv) > 0 and sys.argv[1].isnumeric():
        userid = int(sys.argv[1])
        resp = requests.get(
            '{}users/{}'.format(api_url, userid))
        name = resp.json()['username']
        task_resp = requests.get(
            '{}todos/?userId={}'.format(api_url, userid))
        task_json = task_resp.json()
        json_data = {userid: []}
        for i in task_json:
            r = {
                'task': i['title'],
                'completed': i['completed'],
                'username': name,
                }
            json_data[userid].append(r)
        with open('{}.json'.format(userid), 'w') as jsonfile:
            json.dump(json_data, jsonfile)
