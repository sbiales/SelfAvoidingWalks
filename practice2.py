# simulate self avoiding walk in indefinite lattice
# (0,0) is exactly in the middle of the lattice (50 steps in each direction)
# simulation stops when walker is trapped (ie all directions visited or border)
# max of 5000 steps

import random
import statistics

lengthList = []		    # List holding walk lengths for each simulation
distanceList = []       # List holding the distances from starting point for each simulation
latSizeList = []    # List holding the lattice sizes for each simulation

# Run 10 simulations
for i in range(0, 10):
    lattice =  []		# Initialize the lattice as an empty list of points visited
    length = 0		    # Length of a single walk, used as a control variable

    #Set (0,0), the starting point, to "visited" by appending it to the list of known lattice points
    lattice.append((0,0))
    length += 1

    startx = 0          # Keep track of starting x-coordinate
    starty = 0          # Keep track of starting y-coordinate
    curx = startx		# Initialize current x-coordinate to 0
    cury = starty		# Initialize current y-coordinate to 0

    while(length <= 5000) :
        moves = []		#Create a list of the available next moves, which is initially empty

        # x and y denote temporary positions that we can check to see if they're available
        # First check to see if this is an unvisited position (it's not in the lattice yet)
        # Then if this position is unvisited, add this position as a tuple to the list of available moves

        #check left
        x = curx - 1
        y = cury
        if (x,y) not in lattice :
            moves.append((x,y))

        #check right
        x = curx + 1
        if (x,y) not in lattice :
            moves.append((x,y))

        #check up
        x = curx
        y = cury + 1
        if (x,y) not in lattice :
            moves.append((x,y))

        #check down
        y = cury - 1
        if (x,y) not in lattice :
            moves.append((x,y))

        # Now that we've made a list of available moves, let's check to see if there are any available moves.
        if moves == [] :			# If there are no available moves then, we quit
            print("No more available moves")
            break

        else :				# If there are indeed available moves, choose one at random
            #choose one move at random
            move = random.choice(moves)

            #update current location
            curx = move[0]			# curx = x-position of randomly chosen move tuple
            cury = move[1]			# cury = y-position of randomly chosen move tuple

            # add that randomly chosen move to the lattice to indicate that it was visited
            lattice.append(move)
            length += 1			# Since we moved to that position, increment the length of the walk

            # Continue with the while loop until there are no available moves

    # Now that this simulation is over, let's run some calculations and output stats about this walk
    # The last known current x and last known current y is that end value for each
    endx = curx
    endy = cury

    # append the length of this walk to the list of walk lengths
    lengthList.append(length)

    # Calculate distance (distance = \x_start - x_end\ + \y_start - x_end\) and add to list of distances
    distance = abs(endx-startx) + abs(endy-starty)
    distanceList.append(distance)

    # Now let's calculate the lattice size finding the min and max x and y coordinates
    # Sort the positions by x coordinates and y coordinates
    sortedX = sorted(lattice, key=lambda tup: tup[0])
    sortedY = sorted(lattice, key=lambda tup: tup[1])

    # Now that the positions are sorted by x and y coordinates, let's find the min and max values
    maxX = (sortedX[-1])[0]
    minX = (sortedX[0][0])

    maxY = (sortedY[-1])[1]
    minY = (sortedY[0][1])

    latSize = (maxX - minX) * (maxY - minY)
    latSizeList.append(latSize)

    # Now print the stats for this walk
    print("Iteration #", i, "\t : Distance ", distance, ", Lattice size ", latSize)

    # Now continue the for loop until all 100 iterations are done

# Now that the 100 iterations are done, calculate and print the stats for distance and lattice size
distMean = statistics.mean(distanceList)
distMed = statistics.median(distanceList)
distVar = statistics.variance(distanceList)
distStd = statistics.stdev(distanceList)

sizeMean = statistics.mean(latSizeList)
sizeMed = statistics.median(latSizeList)
sizeVar = statistics.variance(latSizeList)
sizeStd = statistics.stdev(latSizeList)
print("Distance: Mean {:.2f}; Median {:.2f}; Variance {:.2f}; Standard dev {:.2f}" .format(distMean, distMed, distVar,  distStd))
print("Lattice size: Mean {:.2f}; Median {:.2f}; Variance {:.2f}; Standard dev {:.2f}" .format(sizeMean, sizeMed, sizeVar,  sizeStd))
