# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:08:39 2019

@author: Boyo
"""

import csv

#Load data
with open('2.data', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

    #Because CSV returns each row as a list object, and there is only
    #one row in the data file, so use just that row
    data = data[0]

#Convert all of the strings to integers
for x in range(0, len(data)):
    data[x] = int(data[x])

def calc(data, x, y):
    data[1] = x
    data[2] = y
    for pos in range(0, len(data), 4):
        if data[pos] == 1:
            data[data[pos+3]] = data[data[pos+1]] + data[data[pos+2]]

        elif data[pos] == 2:
            data[data[pos+3]] = data[data[pos+1]] * data[data[pos+2]]

        elif data[pos] == 99:
            break

        else:
            print(f'Data error. Invalid Opcode {data[pos]} {type(data[pos])}')

    return data

#Part 1
check_data = calc(data.copy(), 12, 2)
print(f'Done: {check_data[0]}')

#Part 2
for x in range(0,99):
    for y in range(0, 99):

        test = calc(data.copy(), x, y)

        if test[0] == 19690720:
            print(f'Done: 0: {test[0]}, 1: {x}, 2:{y}, Answer: {100 * x + y}')
            break

    else:
        continue

    break


