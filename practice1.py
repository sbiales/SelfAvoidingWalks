#simulate self avoiding walk in finite 100x100 lattice
#(0,0) is exactly in the middle of the lattice (50 steps in each direction)
#simulation stops when walker is trapped (ie all directions visited or border)

import random
import math

size = 100                  #The desired height and width of the lattice
lattice = {}                #Initializes an empty dictionary to represent the lattice
contin = True               #sets while loop variable to true

iterations = 100            #number of simulations we wish to run
pathLengths = []            #a list that will hold the lengths of each iteration's path
remaining = iterations

while (remaining > 0) :     #while there are more iterations to be run
    length = 0              #reset the path length to 0
    contin = True
    
    #Initialize all locations on lattice to "unvisited", represented by (x,y):0 in the dictionary
    for x in range(int(-(size/2)), int(size/2)) :
        for y in range(int(-(size/2)), int(size/2)) :
            lattice[(x,y)] = 0

    #Set (0,0) to "visited"
    lattice[(0,0)] = 1
    length += 1             #increment the path length

    curx = 0		# Initialize current x-coordinate to 0
    cury = 0		# Initialize current y-coordinate to 0

    while(contin) :

        moves = []          #Create a list of the available next moves, initially empty

        # x and y denote temporary positions in the lattice that we'll use to check if the position next to us is available
        # First check to see if this is a valid position (it's in the lattice)
        # Then if this position is unvisited, add this position as a tuple to the list of available moves
        
        #check left
        x = curx - 1
        y = cury
        if (x,y) in lattice :                   #checks if (x,y) is within the lattice bounds
            if lattice[(x,y)] == 0 :            #checks if the location is unvisited
                moves.append((x,y))             #if within bounds and unvisited, add it to the list of available moves

        #check right
        x = curx + 1
        if (x,y) in lattice :
            if lattice[(x,y)] == 0 :
                moves.append((x,y))

        #check up
        x = curx
        y = cury + 1
        if (x,y) in lattice :
            if lattice[(x,y)] == 0 :
                moves.append((x,y))

        #check down
        y = cury - 1
        if (x,y) in lattice :
            if lattice[(x,y)] == 0 :
                moves.append((x,y))

        if moves == [] :                        #if there are no available moves, stop the while loop
            contin = False
            continue
        #At this point there IS at least one available move

        #choose one move at random
        move = random.choice(moves)

        #update current location
        curx = move[0]
        cury = move[1]

        #mark it as visited and increment the path length
        lattice[move] = 1
        length += 1
        
        #print(move)
    remaining -= 1          #decrement the number of remaining iterations
    
    print("Iteration #", (iterations-remaining), "\t : ", length, " steps taken")
    pathLengths.append(length)          #add the path length of the current iteration to the list

#calculations

#average length
avgLength = sum(pathLengths)/iterations
print("Average path length: ", avgLength)

#std deviation
sqDiffs = []

for l in pathLengths :
    sqDiffs.append(pow((l - avgLength),2))

diffsMean = sum(sqDiffs)/iterations
std = math.sqrt(diffsMean)
print("Standard deviation: ", std)


