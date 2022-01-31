#!/usr/bin/python3

"""
This module gets the todo of a user identified by id
gotten from the api https://jsonplaceholder.typicode.com/users
"""

import requests
import sys

api_url = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    if len(sys.argv) > 0 and sys.argv[1].isnumeric():
        userid = int(sys.argv[1])
        resp = requests.get(
            '{}users/{}'.format(api_url, userid))
        name = resp.json()['name']
        task_resp = requests.get(
            '{}todos/?userId={}'.format(api_url, userid))
        c_task = 0
        task_json = task_resp.json()
        t_len = len(task_json)
        completed_task_str = ''
        for i in task_json:
            if i['completed']:
                c_task += 1
                completed_task_str += ('\t {}\n'.format(i['title']))
        mid_str = ' is done with tasks'
        print('Employee {}{}({}/{}):'.format(name, mid_str, c_task, t_len))
        print(completed_task_str)
