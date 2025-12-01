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
zeroes = 0
for idx,dir in enumerate(dirs):
    
    if dir == "L":
        positions.append(positions[-1] - amounts[idx])
    else:
        positions.append(positions[-1] + amounts[idx])
    if positions[-1]%100 == 0:
        zeroes += 1
print("Part 1 cost " + str(time.time()-ts) + " seconds")

passes = 0
positions_div = [position/100 for position in positions]
positions_round = []
for position in positions_div:
    if position > 0:
        positions_round.append(math.ceil(position))
    else:
        positions_round.append(math.floor(position))

for idx in range(1,len(positions_round)):
    if positions_round[idx] != positions_round[idx-1]:
        if positions_round[idx] == 0 or positions_round[idx-1] == 0 or positions_round[idx] ^ positions_round[idx-1] < 0:
            passes += abs(positions_round[idx-1] - positions_round[idx])-1
        else:
            passes += abs(positions_round[idx-1] - positions_round[idx])

print("You hit the number zero " + str(zeroes) + " times")
print("You passed the number zero " + str(passes) + " times")
print("The total is " + str(zeroes + passes))

print("Part 1 & 2 cost " + str(time.time()-ts) + " seconds")
