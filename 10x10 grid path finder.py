import math
import random

def printgrid(g):
    for line in g:
        print('                                                                                    ', *line)


def print2grids(grid1, grid2):
    for line in range(10):
        print('                             ', *grid1[line],'                             ', *map(pad2, grid2[line]))


def pad2(i):
    return "{0:>3}".format(str(i))


grid = []
for e in range(10):
    list = []
    for i in range(10):
        list += [random.randrange(3)]
    grid += [list]



for line in grid:
    print(line)

costsumgrid = []

for e in range(10):
    list = []
    for i in range(10):
        list += ['X']
    costsumgrid += [list]

directiongrid = []

for e in range(10):
    list = []
    for i in range(10):
        list += ['_']
    directiongrid += [list]





print('Select starting point')

print('Select x value from 0 to 9')
x1 = int(input())
print('Select y value from 0 to 9')
y1 = int(input())
#grid[x1][y1] = 'S'
costsumgrid[y1][x1] = 0



print('Select endpoint')
print('Select x value from 0 to 9')
x2 = int(input())
print('Select y value from 0 to 9')
y2 = int(input())
#grid[x2][y2] = 'E'
#costsumgrid[x2][y2] = 'E'

fastestPathTo = {}

print('select movement budget')
movement = int(input())




def findneighbors(x, y):
    neighbors = []
    if x != 0:
        neighbors += [(x-1, y)]
    if x != 9:
        neighbors += [(x+1, y)]
    if y != 0:
        neighbors += [(x, y-1)]
    if y != 9:
        neighbors += [(x, y+1)]
    return neighbors



def matches_budget(budget, costsum_origin, cost_neighbor):
    if budget == costsum_origin + cost_neighbor:
        return True
    return False


FoundNewTile = 0
def expand(budget):
    FoundNewTile = 0
    for y in range(10):
        for x in range(10):
            if isinstance(costsumgrid[y][x], int):
                neighbors = findneighbors(x, y)
                print(neighbors)
                for neighbor in neighbors:
                    if matches_budget(budget, costsumgrid[y][x], grid[neighbor[1]][neighbor[0]]):
                        if costsumgrid[neighbor[1]][neighbor[0]] == 'X':

                            costsumgrid[neighbor[1]][neighbor[0]] = budget

                            #new tile: [neighbor[1]], [neighbor[0]]
                            #old tile: y,x
                            #record new tile's relation to old tile
                            if neighbor[1] > y:
                                directiongrid[neighbor[1]][neighbor[0]] = "↑"
                            if neighbor[1] < y:
                                directiongrid[neighbor[1]][neighbor[0]] = "↓"
                            if neighbor[0] > x:
                                directiongrid[neighbor[1]][neighbor[0]] = "←"
                            if neighbor[0] < x:
                                directiongrid[neighbor[1]][neighbor[0]] = "→"





                            FoundNewTile = 1

    print2grids(grid, costsumgrid)
    return FoundNewTile

for i in range(movement):
    while True:
        outcome = expand(i)
        if outcome == 0:
            break



# FIND THE PATH NOW


x = x2
y = y2

directionrecord = []
while (x != x1 or y != y1):


    if directiongrid[y][x] == '←':
        directionrecord = ['→'] + directionrecord
        x -= 1
    if directiongrid[y][x] == '→':
        directionrecord = ['←'] + directionrecord
        x += 1
    if directiongrid[y][x] == '↑':
        directionrecord = ['↓'] + directionrecord
        y -= 1
    if directiongrid[y][x] == '↓':
        directionrecord = ['↑'] + directionrecord
        y += 1


print(directionrecord)





#print('grid:')
#printgrid(grid)

#print('costsum:')
#printgrid(costsumgrid)

#print2grids(grid, costsumgrid)