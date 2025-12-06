# assignment 5
import time
import math

ts = time.time()
# uitlezen text bestandje
with open('ass06/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.split('\n')
    input1 = [line.split() for line in input]

operators = input1[:][len(input1)-1]

tr = time.time()
# part 1
temp_operands = input1[:][0:len(input1)-1]

operands1 = [[0 for _ in range(len(temp_operands))] for _ in range(len(temp_operands[0]))]
for i in range(len(temp_operands)):
    for j in range(len(temp_operands[0])):
        operands1[j][i] = int(temp_operands[i][j])

result1 = []
for i in range(len(operators)):
    if operators[i] == "+":
        result1.append(sum(operands1[i]))
    else:
        result1.append(math.prod(operands1[i]))

print("The total result for part 1 is " + str(sum(result1))) # correcte waarde is 5227286044585
t1 = time.time()

# part 2
# hier ben ik te brak voor

# print("The amount of fresh ingredients for part 2 is " + str()) # correcte waarde is 
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**6//1)) + " us;" +
      " Part 2 = " + str(int((t2-t1)*10**6//1)) + " us;" +
      " Total time = " + str(int((t2-ts)*10**6//1)) + " us")
# average van 1 run is ongeveer
# kost 2500 us, 7500 us,  us, 9800 us