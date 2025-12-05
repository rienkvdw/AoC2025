# assignment 5
import time

ts = time.time()
# uitlezen text bestandje
with open('ass05/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.split('\n\n')
    idRanges = input[0].splitlines()
    idRanges = [[int(x) for x in idRange.split('-')] for idRange in idRanges]
    idAvailable = [int(x) for x in input[1].splitlines()]

tr = time.time()
# part 1
freshIngredients1 = 0
for ingredient in idAvailable:
    for idRange in idRanges:
        if ingredient in range(idRange[0],idRange[1]+1):
            freshIngredients1 += 1
            break

print("The amount of fresh ingredients for part 1 is " + str(freshIngredients1)) # correcte waarde is 
t1 = time.time()

# part 2
idRangesSorted = sorted(idRanges, key=lambda x: (x[0],x[1]))

freshRanges = [idRangesSorted[0]]
for idRange in idRangesSorted[1:]:
    newFreshRanges = []
    added = False
    for freshRange in freshRanges:
        if idRange[1] <= freshRange[1]:
            newFreshRanges.append(freshRange)
            added = True
        elif idRange[0] <= freshRange[1]:
            newFreshRanges.append([freshRange[0],idRange[1]])
            added = True
        else:
            newFreshRanges.append(freshRange)
    if not added:
        newFreshRanges.append(idRange)
    freshRanges = newFreshRanges

freshIngredients2 = sum([end-start+1 for start, end in freshRanges])

print("The amount of fresh ingredients for part 2 is " + str(freshIngredients2)) # correcte waarde is 369761800782619
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**3//1)) + " ms;" +
      " Part 2 = " + str(int((t2-t1)*10**6//1)) + " us;" +
      " Total time = " + str(int((t2-ts)*10**3//1)) + " ms")
# average van 1 run is ongeveer
# kost 400 us, 40 ms, 1900 us, 42 ms