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
with open('ass08/input_test.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.split()

tr = time.time()
# part 1
numConnections = 10
junctions = []
for i in range(len(input)):
    junctions.append(Junction([int(x) for x in input[i].split(',')], i))

distances = []
for i in range(0,len(junctions)-1):
    distance = [math.inf]*(i+1)
    for j in range(i+1,len(junctions)):
        distance.append(euclideanDistanceSquared(junctions[i].pos,junctions[j].pos))
    distances.append(distance)
print("distances computed")

for k in range(numConnections):
    current_min = math.inf
    for i in range(len(distances)-1,-1,-1):
        for j in range(len(distances[i])-1,i,-1):
            if distances[i][j] < current_min:
                current_min = distances[i][j]
                current_min_i = i
                current_min_j = j
    distances[current_min_i][current_min_j] = math.inf

    junctions[current_min_i].con.update(junctions[current_min_j].con)
    # junctions[current_min_j].con.update(junctions[current_min_i].con)
    for id in junctions[current_min_i].con:
        junctions[id].con = junctions[current_min_i].con
    if k%100 == 0:
        print(k)
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
    current_min = math.inf
    for i in range(len(distances)-1,-1,-1):
        for j in range(len(distances[i])-1,i,-1):
            if distances[i][j] < current_min:
                current_min = distances[i][j]
                current_min_i = i
                current_min_j = j
    distances[current_min_i][current_min_j] = math.inf
    junctions[current_min_i].con.update(junctions[current_min_j].con)
    junctions[current_min_j].con.update(junctions[current_min_i].con)
    for id in junctions[current_min_i].con:
        junctions[id].con.update(junctions[current_min_i].con)
    for id in junctions[current_min_j].con:
        junctions[id].con.update(junctions[current_min_j].con)
    check = len(junctions[current_min_j].con)
    if k%100 == 0:
        print(k)
    k += 1
print(junctions[current_min_i].pos)
print(junctions[current_min_j].pos)

print("The result for part 2 is " + str(junctions[current_min_i].pos.x*junctions[current_min_j].pos.x)) # correcte waarde is 
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**3//1)) + " us;" +
      " Part 2 = " + str(int((t2-t1)*10**3//1)) + " us;" +
      " Total time = " + str(int((t2-ts)*10**3//1)) + " us")
# average van 1 run is ongeveer
# kost 2500 us, 7500 us,  us, 9800 us