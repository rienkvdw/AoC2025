# assignment 9
import time

ts = time.time()


# uitlezen text bestandje
with open('ass07/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()

tr = time.time()
# part 1

print("The total for part 1 is " + str("empty")) # correcte waarde is 
t1 = time.time()
# part 2



print("The total for part 2 is " + str("empty")) # correcte waarde is 
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**6//1)) + " us;" +
      " Part 2 = " + str(int((t2-t1)*10**6//1)) + " us;" +
      " Total time = " + str(int((t2-ts)*10**6//1)) + " us")

# average van  run is ongeveer
# kost  us,  us,  us, us