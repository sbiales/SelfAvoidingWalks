#simulate self avoiding walk in finite 100x100 lattice
#(0,0) is exactly in the middle of the lattice (50 steps in each direction)
#simulation stops when walker is trapped (ie all directions visited or border)

import random

size = 100
lattice = {}
cont = True

#Initialize all locations on lattice to "unvisited"
for x in range(-(size/2), (size/2)) :
    for y in range(-(size/2), (size/2)) :
        lattice[(x,y)] = 0

#Set (0,0) to "visited"
lattice[(0,0)] = 1

curx = 0
cury = 0

while(contin) :

    moves = []
    #Create a list of the available next moves
    #check left
    x = curx - 1
    y = cury
    if lattice[(x,y)] == 0 :
        moves.append((x,y))

    #check right
    x = curx + 1
    y = cury
    if lattice[(x,y)] == 0 :
        moves.append((x,y))

    #check up
    x = curx
    y = cury + 1
    if lattice[(x,y)] == 0 :
        moves.append((x,y))

    #check down
    x = curx
    y = cury - 1
    if lattice[(x,y)] == 0 :
        moves.append((x,y))

    if moves == [] :
        contin = False
        continue

    #choose one move at random
    move = random.choice(moves)

    #update current location
    curx = move[0]
    cury = move[1]

    #mark it as visited
    lattice[move] = 1




    

