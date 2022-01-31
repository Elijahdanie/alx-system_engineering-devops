#!/usr/bin/python3

"""
This module gets the todo of a user identified by id
gotten from the api https://jsonplaceholder.typicode.com/users
"""

import csv
import requests
import sys

if __name__ == '__main__':
    userid = int(sys.argv[1])
    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(userid))
    name = resp.json()['name']
    task_resp = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(userid))
    c_task = 0
    task_json = task_resp.json()
    with open('{}.csv'.format(userid), 'w', newline='') as csvfile:
        writercsv = csv.writer(
            csvfile, quoting=csv.QUOTE_ALL, quotechar='"')
        for i in task_json:
            r = []
            r.append(userid)
            r.append(name)
            r.append(str(i['completed']))
            r.append(i['title'])
            writercsv.writerow(r)
