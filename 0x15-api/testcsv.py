#!/usr/bin/python3

import csv

colors = ['red', 'black', 'white']

with open('tutorial.csv', 'w', newline='') as csvfile:
    fieldnames = ['number', 'colors']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()
    count = 0
    for color in colors:
        thewriter.writerow({'number':count, 'colors':color})
        count += 1
