# assignment 7
import time

ts = time.time()
# uitlezen text bestandje
with open('ass07/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    diagram = inputstring.split()
    diagram = [[x for x in line] for line in diagram]

tr = time.time()
# part 1 & 2
for i in range(len(diagram[0])):
    if diagram[0][i] == "S":
        start = i
        break

beams = set([start])
routes = [0]*len(diagram[0])
routes[start] += 1
splits = 0
for i in range(len(diagram)-1):
    newBeams = set()
    newRoutes = [0]*len(diagram[0])
    for beam in beams:
        if diagram[i+1][beam] == "^":
            splits += 1
            newBeams.add(beam-1)
            newBeams.add(beam+1)
            newRoutes[beam-1] += routes[beam]
            newRoutes[beam+1] += routes[beam]
        else:
            newBeams.add(beam)
            newRoutes[beam] += routes[beam]
    beams = newBeams
    routes = newRoutes

print("The total for part 1 is " + str(splits) + " which is " + str(splits == 1630)) # correcte waarde is 1630
print("The total for part 2 is " + str(sum(routes)) + " which is " + str(sum(routes) == 47857642990160)) # correcte waarde is 47857642990160
te = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((te-tr)*10**6//1)) + " us;" +
      " Total time = " + str(int((te-ts)*10**6//1)) + " us")
# average van 1 run is ongeveer
# kost 1500 us, 6500 us, 8000 us