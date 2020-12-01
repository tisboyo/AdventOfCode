# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:29:58 2019

@author: Boyo
"""
import csv

#Correct answer was 303

import time
start_time = time.time()
print("Starting %s seconds ---" % (time.time() - start_time))

#Load data
with open('3.data', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

    wire_1 = data[8]
    wire_2 = data[9]

def route_wire(wire):
    position = (0, 0)
    points = list()

    for each in wire:
        direction = each[0:1]
        distance = int(each[1:])

        if direction == "R":
            for _ in range(0, distance):
                position = (position[0], position[1] + 1)
                points.append(position)

        elif direction == "L":
            for _ in range(0, distance):
                position = (position[0], position[1] - 1)
                points.append(position)

        elif direction == "U":
            for _ in range(0, distance):
                position = (position[0] + 1, position[1])
                points.append(position)

        elif direction == "D":
            for _ in range(0, distance):
                position = (position[0] - 1, position[1])
                points.append(position)

        else:
            print("error")
    return points


def find_matching(route_a, route_b):
    matches = list()

    matchset = set(route_a).intersection(route_b)
    matches = list(matchset)

    return matches

#Find the points of each route
route_1 = route_wire(wire_1)
route_2 = route_wire(wire_2)

#Find where they cross
matches = find_matching(route_1, route_2)

#Figure out the distances for each matching point
distances = list()

#Build a list of distances that match
for each in matches:
    distances.append(abs(each[0]) + abs(each[1]))

#Sort so the shortest route is in pos 0
distances.sort()
print(distances)

print('Part 1')
print(f"Shortest Distances is {distances[0]}")



print("Total Run Time %s seconds ---" % (time.time() - start_time))
