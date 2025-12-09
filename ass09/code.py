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
with open('ass09/input_test.txt') as inputfile:    # input lezen en splitten in lines
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

largest_rectangle = max([max(line) for line in rectangles])
print("The value for part 1 is " + str(largest_rectangle) + " which is " + str(largest_rectangle == 4750297200)) # correcte waarde is 4750297200
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

mapped_grid = [[0 for _ in range(len(xmap))] for _ in range(len(ymap))]
for i in range(len(tiles)):
    id1 = (i+1)%len(tiles)
    if tiles[id1].posmap.x > tiles[i].posmap.x:
        for j in range(tiles[i].posmap.x, tiles[id1].posmap.x):
            mapped_grid[tiles[i].posmap.y][j] = 1
    elif tiles[id1].posmap.x < tiles[i].posmap.x:
        for j in range(tiles[i].posmap.x, tiles[id1].posmap.x, -1):
            mapped_grid[tiles[i].posmap.y][j] = 1
    elif tiles[id1].posmap.y > tiles[i].posmap.y:
        for j in range(tiles[i].posmap.y, tiles[id1].posmap.y):
            mapped_grid[j][tiles[i].posmap.x] = 1
    else:
        for j in range(tiles[i].posmap.y, tiles[id1].posmap.y, -1):
            mapped_grid[j][tiles[i].posmap.x] = 1


print("The total for part 2 is " + str("empty")) # correcte waarde is 
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**3//1)) + " ms;" +
      " Part 2 = " + str(int((t2-t1)*10**3//1)) + " ms;" +
      " Total time = " + str(int((t2-ts)*10**3//1)) + " ms")

# average van  run is ongeveer
# kost  us,  us,  us, us