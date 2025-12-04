# assignment 2
import time
import re

ts = time.time()
# uitlezen text bestandje en splitten in firstIDs en lastIDs
with open('ass02/input.txt') as inputfile:    # input lezen en splitten in juiste waardes
    inputstring = inputfile.read()
    y = re.split(r'[,-]',inputstring)
    firstIDs = [int(x) for x in y[0::2]]
    lastIDs = [int(x) for x in y[1::2]]

IDranges = []
for i in range(len(firstIDs)):
    IDranges.append([str(x) for x in range(firstIDs[i],lastIDs[i]+1)])

print("Reading input cost " + str((time.time()-ts)*1000//1) + " ms") # dit kostte al 309 ms

# part 1
invalidIDs1 = []
for IDrange in IDranges:
    for idstr in IDrange:
        digits = len(idstr)
        halfdigits = digits // 2
        if idstr[0:halfdigits] == idstr[halfdigits:digits]:
            invalidIDs1.append(int(idstr))
print("Part 1 cost " + str((time.time()-ts)*1000//1) + " ms") # kostte 812 ms (dus nog net minder dan 1 seconde)

print("The sum of invalid IDs for part 1 is " +  str(sum(invalidIDs1)))

# part 2
invalidIDs2 = []
for IDrange in IDranges:
    for idstr in IDrange:
        # ik heb een mooi stukje regular expressions gevonden
        # ik zocht puur op checking repeating sequence string en toen kwam geeksforgeeks met de oplossing
        if bool(re.fullmatch(r"(.+)\1+",idstr)):
            invalidIDs2.append(int(idstr))
print("Part 2 cost " + str((time.time()-ts)*1000//1) + " ms") # kostte 2092 ms (dus meer dan 1 seconde :( )

print("The sum of invalid IDs for part 2 is " +  str(sum(invalidIDs2)))