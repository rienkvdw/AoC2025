# assignment 1
import math
import copy
import time
import numpy
import itertools
import re

# uitlezen text bestandje
with open('ass01/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()



dirs = []
amounts = []
for lines in input:                     # splitten op de gehele set waar ik voor wil checken
    y = re.findall(r'[A-Za-z]+|\d+', lines)       # met regular expression
    dirs.append(y[0])
    amounts.append(int(y[1]))

ts = time.time()
# part 1
positions = []
positions.append(50)
for id,dir in enumerate(dirs):
    if dir == "L":
        positions.append(positions[-1] - amounts[id])
    else:
        positions.append(positions[-1] + amounts[id])

zeroes = 0
for position in positions:
    if position%100 == 0:
        zeroes += 1
print("You hit the number zero " + str(zeroes) + " times")

print("Deel 1 kostte " + str(time.time()-ts) + " seconden")
