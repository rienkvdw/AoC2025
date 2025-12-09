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
        self.posmap = Coordinate(coords)
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
print("The value for part 1 is " + str(largestRectangle) + " which is " + str(largestRectangle == 4750297200)) # correcte waarde is 4750297200
t1 = time.time()

# part 2
# we gaan wat proberen. De getalletjes zijn te groot, dus we mappen ze naar kleinere getallen
xs = set()
ys = set()
# eerst alle x en y coordinaten vinden
for i in range(len(lines)):
    coord = [int(x) for x in lines[i].split(',')]
    xs.add(coord[0])
    ys.add(coord[1])
# dan die allemaal in een map gooien (met dict)
xmap = {xcoord: idmap for idmap, xcoord in enumerate(sorted(xs))}
ymap = {ycoord: idmap for idmap, ycoord in enumerate(sorted(ys))}
# dan die waardes toevoegen aan posities van dingen
for tile in tiles:
    tile.posmap.x = xmap[tile.pos.x]
    tile.posmap.y = ymap[tile.pos.y]


print("The total for part 2 is " + str("empty")) # correcte waarde is 
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**3//1)) + " ms;" +
      " Part 2 = " + str(int((t2-t1)*10**3//1)) + " ms;" +
      " Total time = " + str(int((t2-ts)*10**3//1)) + " ms")

# average van  run is ongeveer
# kost  us,  us,  us, us