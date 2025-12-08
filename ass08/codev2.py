# assignment 5
import time
import numpy
import math

class Coordinate:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self = (self.x,self.y,self.z)
    def __str__(self):
        return str((self.x,self.y,self.z))
    def __repr__(self):
        return str((self.x,self.y,self.z))

class Junction:
    def __init__(self, coords, id):
        self.pos = Coordinate(coords)
        self.dis = []
        self.con = {id}
    def __str__(self):
        return str((self.pos,self.con))
    def __repr__(self):
        return str((self.pos,self.con))

def euclideanDistanceSquared(coordinate1, coordinate2):
    return int((coordinate1.x-coordinate2.x)**2 +
               (coordinate1.y-coordinate2.y)**2 +
               (coordinate1.z-coordinate2.z)**2)

ts = time.time()
# uitlezen text bestandje
with open('ass08/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.split()

tr = time.time()
# part 1
numConnections = 1000
junctions = []
for i in range(len(input)):
    junctions.append(Junction([int(x) for x in input[i].split(',')], i))

distancesID = []
for i in range(0,len(junctions)-1):
    for j in range(i+1,len(junctions)):
        distancesID.append((euclideanDistanceSquared(junctions[i].pos,junctions[j].pos),i,j))
distancesIDSorted = sorted(distancesID, key=lambda x: x[0])
print("distances computed")

for k in range(numConnections):
    distancesIDSorted[k][0]
    junction1_id = distancesIDSorted[k][1]
    junction2_id = distancesIDSorted[k][2]
    junctions[junction1_id].con.update(junctions[junction2_id].con)
    for id in junctions[junction1_id].con:
        junctions[id].con = junctions[junction1_id].con
print("first " + str(numConnections) +  " connections made")

circuits = []
for i in range(len(junctions)):
    if junctions[i].con not in circuits:
        circuits.append(junctions[i].con)
circuitsSorted = sorted(circuits, key = lambda x : (len(x)))

print("The total result for part 1 is " + str(len(circuitsSorted[-1])*len(circuitsSorted[-2])*len(circuitsSorted[-3]))) # correcte waarde is 123930
t1 = time.time()

# part 2
check = len(junctions[0].con)
while(check != len(junctions)):
    distancesIDSorted[k][0]
    junction1_id = distancesIDSorted[k][1]
    junction2_id = distancesIDSorted[k][2]
    junctions[junction1_id].con.update(junctions[junction2_id].con)
    for id in junctions[junction1_id].con:
        junctions[id].con = junctions[junction1_id].con
    check = len(junctions[junction1_id].con)
    k += 1

print("The result for part 2 is " + str(junctions[junction1_id].pos.x*junctions[junction2_id].pos.x)) # correcte waarde is 27338688
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**3//1)) + " ms;" +
      " Part 2 = " + str(int((t2-t1)*10**3//1)) + " ms;" +
      " Total time = " + str(int((t2-ts)*10**3//1)) + " ms")
# average van 1 run is ongeveer
# kost 150 us, 900 ms, 1000 ms, 1900 ms