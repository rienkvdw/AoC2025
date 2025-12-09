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

# dit gebruik ik bij deel 2, dus heb hier naartoe verplaatst zodat ik die andere niet meer nodig heb
areas = []
for i in range(len(tiles)-1):
    for j in range(i+1,len(tiles)):
        areas.append((rectangleArea(tiles[i].pos,tiles[j].pos),i,j))
areas_sorted = sorted(areas, key = lambda x : x[0], reverse=True)

largest_rectangle1 = areas_sorted[0][0]
print("The value for part 1 is " + str(largest_rectangle1) + " which is " + str(largest_rectangle1 == 4750297200)) # correcte waarde is 4750297200
t1 = time.time()

# part 2
# de slimme dingen die ik had bedacht waren niet nuttig :(

# we gaan door alle areas heen
for area in areas_sorted:
    corner0 = tiles[area[1]]
    corner1 = tiles[area[2]]
    xmin, xmax = min([corner0.pos.x,corner1.pos.x]), max([corner0.pos.x,corner1.pos.x])
    ymin, ymax = min([corner0.pos.y,corner1.pos.y]), max([corner0.pos.y,corner1.pos.y])

    cross = False
    # we beginnen bij de id van corner0, want grote kans dat er in de buurt van een corner wat dingen gebeuren die het verneuken voor die corner
    for i in range(corner0.id, len(tiles) + corner0.id):
        id0 = i%len(tiles)
        id1 = (i+1)%len(tiles)
        tile0_pos = tiles[id0].pos
        tile1_pos = tiles[id1].pos
        # hier is heel wat geoptimaliseerd qua checks, dus leesbaar is het niet meer
        if (tile0_pos.x == tile1_pos.x):
            if (xmin < tile0_pos.x < xmax) and (tile0_pos.y > ymin or tile1_pos.y > ymin) and (tile0_pos.y < ymax or tile1_pos.y < ymax):
                cross = True
                break
        elif (tile0_pos.y == tile1_pos.y):
            if (ymin < tile0_pos.y < ymax) and (tile0_pos.x > xmin or tile1_pos.x > xmin) and (tile0_pos.x < xmax or tile1_pos.x < xmax):
                cross = True
                break
    if not cross:
        largest_rectangle2 = area[0]
        break

print("The value for part 2 is " + str(largest_rectangle2) + " which is " + str(largest_rectangle2 == 1578115935)) # correcte waarde is 1578115935
t2 = time.time()

print("Timing: Inputs = " + str(int((tr-ts)*10**6//1)) + " us;" +
      " Part 1 = " + str(int((t1-tr)*10**3//1)) + " ms;" +
      " Part 2 = " + str(int((t2-t1)*10**3//1)) + " ms;" +
      " Total time = " + str(int((t2-ts)*10**3//1)) + " ms")

# average van 1 run is ongeveer
# kost 100 us, 120 ms, 2900 ms, 3100 ms