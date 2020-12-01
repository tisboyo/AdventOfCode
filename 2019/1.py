# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 01:22:53 2019

@author: Boyo
"""

'''
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

Part 2 adds adding the weight caused by the additional fuel
'''

import math

sum_of_masses = 0

def fuel_calc(fuel : int):
    '''
    Calculates the fuel needed based on the mass, recursively adding more
    to compensate for the additional fuel
    '''

    fuel = math.floor(int(fuel) / 3) - 2

    if fuel <= 0:
        return 0

    else:
        return (fuel + fuel_calc(fuel))

#Read data
with open('1.data') as f:
    mass_list = f.read().splitlines()

#mass_list = [1969, 100756] #Expect: 966, 50346

#Loop through the data, adding all requirements to sum_of_masses
for mass in mass_list:
    fuel = fuel_calc(mass)

    sum_of_masses += fuel

    print(f'Mass: {mass}, Fuel: {fuel}')

print(f'Sum: {sum_of_masses}')

