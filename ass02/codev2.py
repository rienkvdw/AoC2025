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

print("The sum of invalid IDs for part 1 is " +  str(sum(invalidIDs1))) # 19386344315

# part 2
invalidIDs2 = []
for IDrange in IDranges:
    for idstr in IDrange:
        # dit is een poging zonder de regex, maar de verwachting is dat die veel langer runt
        digits = len(idstr)
        digitsdiv = [int(digits/x) for x in range(1,digits//2+1) if digits/x%1==0]

        for div in digitsdiv:
            digs = digits//div
            idstrsliced = [idstr[i*digs:(i+1)*digs] for i in range(0,div)]
            if len(set(idstrsliced)) == 1:
                invalidIDs2.append(int(idstr))
                break
    else:
        continue
    break

print("Part 2 cost " + str((time.time()-ts)*1000//1) + " ms") # eigen meer beun oplossing kost 8221 ms

print("The sum of invalid IDs for part 2 is " +  str(sum(invalidIDs2))) # 34421651192