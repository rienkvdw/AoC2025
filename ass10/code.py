# assignment 10
import time
import itertools
import math

ts = time.time()
# uitlezen text bestandje
with open('ass10/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input_lines = inputstring.split('\n')

lights = []
bitwise_lights = []
buttons = []
bitwise_buttons = []
joltages = []
for line in input_lines:
    contents = line.split()
    lights.append([int(c == '#') for c in contents[0][1:-1]])
    bitwise_light = 0
    for b in range(len(lights[-1])):
        bitwise_light += lights[-1][b]*2**(len(lights[-1])-b-1)
    bitwise_lights.append(bitwise_light)

    buttons.append([])
    bitwise_buttons.append([])
    joltages.append([int(c) for c in contents[-1][1:-1].split(',')])

    for content in contents[1:-1]:
        button = [0]*len(lights[-1])
        for c in content[1:-1].split(','):
            button[int(c)] += 1
        buttons[-1].append(button)

        bitwise_button = 0
        for b in range(len(button)):
            bitwise_button += button[b]*(2**(len(button)-b-1))
        bitwise_buttons[-1].append(bitwise_button)

tr = time.time()
# part 1
shortest = []
for i in range(len(lights)):
    shortest.append(len(bitwise_buttons[i]))
    for path in range(len(bitwise_buttons[i])-1,-1,-1):
        for order in itertools.combinations(bitwise_buttons[i],len(bitwise_buttons[i])-path):
            lights_current = 0
            for j in range(len(order)):
                lights_current = lights_current ^ order[j]
                if j >= shortest[-1]:
                    break
                elif lights_current == bitwise_lights[i]:
                    shortest[-1] = j
                    break
            if shortest[-1] == 0:
                break
            else:
                continue
    shortest[-1] += 1


print("The total for part 1 is " + str(sum(shortest))) # correcte waarde is 
t1 = time.time()
# part 2



print("The total for part 2 is " + str("empty")) # correcte waarde is 
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**3//1)) + " ms;" +
      " Part 1 = " + str(int((t1-tr)*10**3//1)) + " ms;" +
      " Part 2 = " + str(int((t2-t1)*10**6//1)) + " us;" +
      " Total time = " + str(int((t2-ts)*10**6//1)) + " us")

# average van  run is ongeveer
# kost  us,  us,  us, us