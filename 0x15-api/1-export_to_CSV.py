#!/usr/bin/python3

"""
This module gets the todo of a user identified by id
gotten from the api https://jsonplaceholder.typicode.com/users
"""

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
    # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    with open('USER_ID.csv', 'w', newline='') as csvfile:
        h = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writercsv = csv.DictWriter(csvfile, fieldnames=h)
        writercsv.writeheader()
        for i in task_json:
            r = {}
            r['USER_ID'] = userid
            r['USERNAME'] = name
            r['TASK_COMPLETED_STATUS'] = i['completed']
            r['TASK_TITLE'] = i['title']
            writercsv.writerow(r)
