#simulate self avoiding walk in finite 100x100 lattice
#(0,0) is exactly in the middle of the lattice (50 steps in each direction)
#simulation stops when walker is trapped (ie all directions visited or border)

import random
import numpy

lengthList = []		# List holding walk lengths for each simulation
size = 100		# Size of lattice, used to initialize lattice

# Run 100 simulations
for i in range(1, 100):
    lattice = {}		# Initialize the lattice as an empty dictionary
    contin = True		# Control variable for while loop
    length = 0		# Length of walk


    #Initialize all locations on lattice to "unvisited", where 0 means unvisited, and 1 means visited
    for x in range(int(-(size/2)), int(size/2)) :
        for y in range(int(-(size/2)), int(size/2)) :
            lattice[(x,y)] = 0

    #Set (0,0) to "visited"
    lattice[(0,0)] = 1
    length += 1

    curx = 0		# Initialize current x-coordinate to 0
    cury = 0		# Initialize current y-coordinate to 0

    while(contin) :

        moves = []		#Create a list of the available next moves, which is initially empty

        # x and y denote temporary positions in the lattice that we'll use to check if the position next to us is available
        # First check to see if this is a valid position (it's in the lattice)
        # Then if this position is unvisited, add this position as a tuple to the list of available moves

        #check left
        x = curx - 1
        y = cury
        if (x,y) in lattice :
            if lattice[(x,y)] == 0 :
                moves.append((x,y))

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

        # Now that we've made a list of available moves, let's check to see if there are any available moves.
        if moves == [] :			# If there are no available moves then, we quit
            contin = False
            continue
        else :				# If there are indeed available moves, choose one at random
            #choose one move at random
            move = random.choice(moves)

            #update current location
            curx = move[0]			# curx = x-position of randomly chosen move tuple
            cury = move[1]			# cury = y-position of randomly chosen move tuple

            #mark that randomly chosen position as visited in the lattice
            lattice[move] = 1
            length += 1			# Since we moved to that position, increment the length of the walk

    print("Chose position", move)	# Display the position we chose to move to
    # Continue with the while loop until there are no available moves

    # Now that are no available moves left, output the length of the walk
    print(length, "steps taken in this walk")

    # Now that this simulation is over, append the length of this walk to the list of walk lengths
    lengthList.append(length)
    # Now continue the for loop until all 100 iterations are done

# Now that the 100 iterations are done, print the mean of the lengths of those walk lengths 
print(numpy.mean(lengthList))
