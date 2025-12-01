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
    if y[0] == "L":
        amounts.append(int(y[1])*-1)
    else:
        amounts.append(int(y[1]))
    dirs.append(y[0])

ts = time.time()
# part 1
positions = []
positions.append(50)
zeros = 0
for idx,dir in enumerate(dirs):
    positions.append(positions[-1] + amounts[idx])
    if positions[-1]%100 == 0:
        zeros += 1
print("You hit the number zero " + str(zeros) + " times")
print("Part 1 cost " + str(time.time()-ts) + " seconds")

ts = time.time()
# part 2 ging niet goed maar kon ook geen tips vinden :(
position = 50
passes = 0
for amount in amounts:
    new_position = position + amount
    if new_position > 0:
        passes += new_position//100
    elif new_position == 0:
        passes += 1
    else:
        passes += ((100-position)%100 + abs(amount)) // 100
    position = new_position % 100

print("You passed the number zero " + str(passes-zeros) + " times")
print("Part 2 cost " + str(time.time()-ts) + " seconds")

print("Total is " + str(passes))
