# assignment 4
import math
import copy
import time
import numpy
import itertools
import re

# coordinate class van vorig jaar, hopelijk is het nuttig
class Coordinate:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self = (self.x,self.y)
    def __str__(self):
        return str((self.x,self.y))
    def __repr__(self):
        return str((self.x,self.y))

ts = time.time()
# uitlezen text bestandje
with open('ass04/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    grid = [list(line) for line in input]

tr = time.time()
# part 1
numgrid = numpy.pad([[int(bool(x == "@")) for x in gridline] for gridline in grid], (1,1))
movablepapers1 = 0
for i in range(1,len(numgrid)-1):
    for j in range(1,len(numgrid[i])-1):
        if numgrid[i,j] == 1:
            movablepapers1 += int(sum(sum(numgrid[i-1:i+2,j-1:j+2])) < 5)

print("The amount of movable papers for part 1 is " + str(movablepapers1)) # correcte waarde is 1516
t1 = time.time()

# part 2
# Peter had het goede idee om een kernel te gebruiken, ik denk dat dat efficienter zou kunnen zijn dus dat ga ik ook doen
# kernel met -1 voor alle boxes, 4 is omdat het minder dan 4 moet zijn. Op deze manier als er een box is is het 4 - n,
# waarbij n het aantal dozen eromheen is. Dit maakt dat alle gevallen met een positief aantal dozen een positieve output krijgen
kernel = numpy.array([[-1, -1, -1],
                      [-1,  4, -1],
                      [-1, -1, -1]])
numgrid =  numpy.pad(numpy.array([[int(x == "@") for x in gridline] for gridline in grid]),(1,1))
numgrid_res = numpy.copy(numgrid)
movablepapers2 = numpy.sum(numgrid)

removed = True
while (removed):
    removed = False
    for i in range(1,len(numgrid)-1):
        for j in range(1,len(numgrid[0])-1):
            # we gebruiken numpy.sum omdat die 2d summed en dat is goed en mooi
            if numpy.sum(numgrid[i-1:i+2,j-1:j+2]*kernel) > 0:
                removed = True
                numgrid[i][j] = 0

movablepapers2 -= numpy.sum(numgrid)

print("The amount of movable papers for part 2 is " + str(movablepapers2)) # correcte waarde is 9122
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**3//1)) + " ms;" +
      " Part 2 = " + str(int((t2-t1)*10**3//1)) + " ms;" +
      " Total time = " + str(int((t2-ts)*10**3//1)) + " ms")
# average van 1 run is ongeveer
# kost 1400 us, 65 ms, 6100 ms, 6200 ms