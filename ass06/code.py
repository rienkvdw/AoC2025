# assignment 5
import time
import math

ts = time.time()
# uitlezen text bestandje
with open('ass06/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.split('\n')
    input_split = [line.split() for line in input]

operators = input_split[:][len(input_split)-1]

tr = time.time()
# part 1
temp_operands = input_split[:][0:len(input_split)-1]

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
# niet meer brak :)
prev_operator = len(input[0])+1
numNumbers = len(input)-1
result2 = []
for i in range(len(input[0])-1,-1,-1):
    if input[numNumbers][i] == "+":
        numbers = [0]*(prev_operator-i-1)
        for j in range(prev_operator-2,i-1,-1):             # honestly, hier gebeurt iets te veel random bullshit qua indexing, dit werktte uiteindelijk
            for k in range(numNumbers):
                if input[k][j].isdigit():
                    numbers[j-i] = numbers[j-i]*10 + int(input[k][j])
        result2.append(sum(numbers))
        prev_operator = i
    elif input[numNumbers][i] == "*":
        numbers = [0]*(prev_operator-i-1)
        for j in range(prev_operator-2,i-1,-1):
            for k in range(numNumbers):
                if input[k][j].isdigit():
                    numbers[j-i] = numbers[j-i]*10 + int(input[k][j])
        result2.append(math.prod(numbers))
        prev_operator = i

print("The total result for part 2 is " + str(sum(result2))) # correcte waarde is 10227753257799
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**6//1)) + " us;" +
      " Part 2 = " + str(int((t2-t1)*10**6//1)) + " us;" +
      " Total time = " + str(int((t2-ts)*10**6//1)) + " us")
# average van 3 runs is ongeveer
# kost 800 us, 3500 us, 15000 us, 19000 us