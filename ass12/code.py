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
        self.quantities = [int(c) for c in splitline[1:]]
        self.quantity = sum(self.quantities)
        self.tracker = 0.5
    def __str__(self):
        return ((self.size, self.quantity))
    def __repr__(self):
        return str((self.size, self.quantity))

ts = time.time()
# uitlezen text bestandje
with open('ass12/input.txt') as inputfile:    # input lezen en splitten in lines
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

tr = time.time()
# part 1
print("The total amount of regions is " + str(len(regions)))
print('\n' + "First checking all regions where total present area is greater than region area, which are all not possible")
for region in regions:
    required_area = 0
    for i in range(len(presents)):
        required_area += region.quantities[i]*presents[i].area
    if required_area > region.area:
        region.tracker = 0

print("After removing all regions which are definitely not possible there are " + str(sum([1  for region in regions if region.tracker == 0.5])) + " left to check")
print('\n' + "Next checking all regions where all presents get their own 3x3 area")
for region in regions:
    if region.tracker != 0:
        x_reduced = region.x // 3
        y_reduced = region.y // 3
        allowed_quantity = x_reduced * y_reduced
        if allowed_quantity >= region.quantity:
            region.tracker = 1

print("After removing all regions which are definitely possible there are " + str(sum([1  for region in regions if region.tracker == 0.5])) + " left to check")

if sum([1 for region in regions if region.tracker == 0.5]) == 0:
    print('\n' + "All regions checked and classified")
    print("The total for part 1 is " + str(sum([region.tracker for region in regions]))) # correcte waarde is 550
else:
    print('\n' + "All regions checked, but not all could be classified")
    print("The total for checked regions is " + str(sum([region.tracker for region in regions if region.tracker != 0.5])))
t1 = time.time()
# part 2

print('\n' + "Er is geen part 2 :)")
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**6//1)) + " us;" +
      " Total time = " + str(int((t2-ts)*10**6//1)) + " us")

# average van 5 run is ongeveer
# kost 4700 us, 2500 us, 6500 us