# assignment 9
import time

class Coordinate:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self = (self.x,self.y)
    def __str__(self):
        return str((self.x,self.y))
    def __repr__(self):
        return str((self.x,self.y))

class Tile:
    def __init__(self, coords, id):
        self.pos = Coordinate(coords)
        self.id = id
    def __str__(self):
        return str((self.pos,self.id))
    def __repr__(self):
        return str((self.pos,self.id))

def rectangleArea(coordinate1, coordinate2):
    return (abs(coordinate1.x-coordinate2.x)+1)*(abs(coordinate1.y-coordinate2.y)+1)

ts = time.time()
# uitlezen text bestandje
with open('ass09/input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    lines = inputstring.split()

tr = time.time()
# part 1
tiles = []
for i in range(len(lines)):
    tiles.append(Tile([int(x) for x in lines[i].split(',')], i))

rectangles = []
for i in range(len(tiles)):
    rectangle = []
    for j in range(i):
        rectangle.append(rectangles[j][i])
    rectangle.append(1)
    for j in range(i+1,len(tiles)):
        rectangle.append(rectangleArea(tiles[i].pos,tiles[j].pos))
    rectangles.append(rectangle)

largestRectangle = max([max(line) for line in rectangles])
print("The value for part 1 is " + str(largestRectangle) + " which is " + str(largestRectangle == 4750297200)) # correcte waarde is 
t1 = time.time()

# part 2



print("The total for part 2 is " + str("empty")) # correcte waarde is 
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**3//1)) + " ms;" +
      " Part 2 = " + str(int((t2-t1)*10**6//1)) + " us;" +
      " Total time = " + str(int((t2-ts)*10**3//1)) + " ms")

# average van  run is ongeveer
# kost  us,  us,  us, us