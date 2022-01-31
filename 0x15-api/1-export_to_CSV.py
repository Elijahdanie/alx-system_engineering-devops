#!/usr/bin/python3

"""
This module gets the todo of a user identified by id
gotten from the api https://jsonplaceholder.typicode.com/users
"""

import csv
import requests
import sys

api_url = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    if len(sys.argv) > 0 and sys.argv[1].isnumeric():
        userid = int(sys.argv[1])
        resp = requests.get(
            '{}users/{}'.format(api_url, userid))
        if resp.status_code == 200:
            name = resp.json()['username']
            task_resp = requests.get(
                '{}todos/?userId={}'.format(api_url, userid))
            task_json = task_resp.json()
            with open('{}.csv'.format(userid), 'w', newline='') as csvfile:
                writercsv = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for i in task_json:
                    r = []
                    r.append(userid)
                    r.append(name)
                    r.append(str(i['completed']))
                    r.append(i['title'])
                    writercsv.writerow(r)
