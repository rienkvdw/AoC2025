# assignment 12
import time

class Shape:
    def __init__(self, lines):
        shape = []
        area = 0
        for line in lines:
            shape.append([int(c == '#') for c in line])
            area += sum(shape[-1])
        self.shape = shape
        self.area = area
    def __str__(self):
        return str(self.shape)
    def __repr__(self):
        return str((self.shape,self.area))

class Region:
    def __init__(self, splitline):
        xy = splitline[0].split('x')
        self.x = int(xy[0])
        self.y = int(xy[1][0:-1])
        self.size = (self.x, self.y)
        self.area = self.x*self.y
        self.quantity = [int(c) for c in splitline[1:]]
    def __str__(self):
        return ((self.size, self.quantity))
    def __repr__(self):
        return str((self.size, self.quantity))

ts = time.time()
# uitlezen text bestandje
with open('ass12/input_test.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    lines = inputstring.split('\n')
    lines = [line for line in lines if line.strip()]
    presents = []
    regions = []
    for i in range(len(lines)):
        if lines[i][1] == ':':
            present = Shape(lines[i+1:i+4])
            presents.append(present)
        elif lines[i][0].isdigit():
            regions.append(Region(lines[i].split()))

print(present)
print()
print(regions)

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