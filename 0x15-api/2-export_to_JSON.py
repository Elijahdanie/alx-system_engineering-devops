#!/usr/bin/python3

"""
This module gets the todo of a user identified by id
gotten from the api https://jsonplaceholder.typicode.com/users
"""

import json
import requests
import sys
import csv

if __name__ == '__main__':
    userid = int(sys.argv[1])
    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(userid))
    name = resp.json()['name']
    task_resp = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(userid))
    c_task = 0
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
