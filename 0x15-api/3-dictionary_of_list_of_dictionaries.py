#!/usr/bin/python3

"""
This module gets the todo of a user identified by id
gotten from the api https://jsonplaceholder.typicode.com/users
"""

import json
import requests

if __name__ == '__main__':
    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    json_all_users = resp.json()
    all_data = {}
    for user in json_all_users:
        name = user['username']
        userid = user['id']
        print(userid)
        task_resp = requests.get(
            'https://jsonplaceholder.typicode.com/todos'.format(userid))
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
