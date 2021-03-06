#!/usr/bin/python3

"""
This module gets the todo of a user identified by id
gotten from the api https://jsonplaceholder.typicode.com/users
"""

import json
import requests

api_url = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    resp = requests.get(
        '{}users'.format(api_url))
    json_all_users = resp.json()
    all_data = {}
    for user in json_all_users:
        name = user['username']
        userid = user['id']
        task_resp = requests.get(
            '{}todos/?userId={}'.format(api_url, userid))
        c_task = 0
        task_json = task_resp.json()
        json_data = []
        for i in task_json:
            r = {
                'username': name,
                'task': i['title'],
                'completed': i['completed'],
                }
            json_data.append(r)
        all_data[userid] = json_data
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_data, jsonfile)
